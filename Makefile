# Workiva SDK Generation Pipeline
# ================================
# Usage:
#   make download       - Download latest specs (requires SPEC_URLS configured)
#   make check          - Check if specs changed since last generation
#   make generate       - Generate models + operations from OAS specs
#   make generate-models     - Generate Pydantic models only
#   make generate-operations - Generate operation namespaces only
#   make all            - Download + check + generate (only if changed)
#   make force          - Force regeneration regardless of changes
#
# Configure download URLs in spec_sources.conf

SHELL := /bin/bash
.PHONY: all download check generate generate-models generate-operations force clean help test test-unit test-integration test-cov build publish

# Directories
SPECS_DIR := oas
SCRIPTS_DIR := scripts
SDK_DIR := workiva-sdk
CHECKSUMS_FILE := .spec_checksums

# Source specs
SPEC_NAMES := platform.yaml chains.yaml wdata.yaml
SPECS := $(addprefix $(SPECS_DIR)/,$(SPEC_NAMES))

# Config file for download URLs
SOURCES_CONF := spec_sources.conf

# User-Agent required by developers.workiva.com (rejects bare curl)
CURL_UA := Mozilla/5.0 (compatible; WorkivaSDKBot/1.0)

# ---- Main targets ----

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: download check-and-generate ## Download specs and regenerate if changed

force: generate ## Force full regeneration

generate-if-changed: check-and-generate ## Only regenerate if specs changed

# ---- Download ----

download: $(SOURCES_CONF) ## Download latest specs from configured URLs
	@echo "⬇ Downloading specs..."
	@while IFS='=' read -r name url; do \
		[ -z "$$name" ] && continue; \
		[[ "$$name" =~ ^# ]] && continue; \
		url=$$(echo "$$url" | xargs); \
		name=$$(echo "$$name" | xargs); \
		echo "  Fetching $$name from $$url"; \
		curl -sSfL -H "User-Agent: $(CURL_UA)" "$$url" -o "$(SPECS_DIR)/$$name" || \
			(echo "  FAILED to download $$name" && exit 1); \
	done < $(SOURCES_CONF)
	@echo "✓ All specs downloaded"

$(SOURCES_CONF):
	@echo "# Workiva OpenAPI Spec Download URLs" > $@
	@echo "# Format: filename = URL" >> $@
	@echo "# Uncomment and fill in the URLs when available" >> $@
	@echo "" >> $@
	@echo "# platform.yaml = https://developers.workiva.com/path/to/platform-spec.yaml" >> $@
	@echo "# chains.yaml = https://developers.workiva.com/path/to/chains-spec.yaml" >> $@
	@echo "# wdata.yaml = https://developers.workiva.com/path/to/wdata-spec.yaml" >> $@
	@echo ""
	@echo "Created $(SOURCES_CONF) - edit it with your download URLs"

# ---- Change detection ----

check: ## Check if specs changed since last generation
	@if [ ! -f $(CHECKSUMS_FILE) ]; then \
		echo "No previous checksums found - generation needed"; \
		exit 1; \
	fi
	@current=$$(sha256sum $(SPECS) 2>/dev/null | sort | sha256sum | cut -d' ' -f1); \
	previous=$$(cat $(CHECKSUMS_FILE) 2>/dev/null); \
	if [ "$$current" = "$$previous" ]; then \
		echo "✓ No changes detected"; \
		exit 0; \
	else \
		echo "⚠ Specs have changed - regeneration needed"; \
		exit 1; \
	fi

save-checksums:
	@sha256sum $(SPECS) 2>/dev/null | sort | sha256sum | cut -d' ' -f1 > $(CHECKSUMS_FILE)
	@echo "✓ Checksums saved"

check-and-generate:
	@current=$$(sha256sum $(SPECS) 2>/dev/null | sort | sha256sum | cut -d' ' -f1); \
	previous=$$(cat $(CHECKSUMS_FILE) 2>/dev/null || echo "none"); \
	if [ "$$current" = "$$previous" ]; then \
		echo "✓ No changes - skipping generation"; \
	else \
		echo "⚠ Changes detected - regenerating SDK..."; \
		$(MAKE) generate; \
	fi

# ---- Generation ----

generate: ## Generate models + operations from OAS specs
	@echo "🐍 Generating SDK (models + operations)..."
	cd $(SDK_DIR) && uv run python ../$(SCRIPTS_DIR)/generate_sdk.py
	@$(MAKE) save-checksums
	@echo ""
	@echo "✓ SDK generated in $(SDK_DIR)/"

generate-models: ## Generate Pydantic models only
	@echo "🐍 Generating models..."
	cd $(SDK_DIR) && uv run python ../$(SCRIPTS_DIR)/generate_sdk.py --models-only

generate-operations: ## Generate operation namespaces only
	@echo "🐍 Generating operations..."
	cd $(SDK_DIR) && uv run python ../$(SCRIPTS_DIR)/generate_sdk.py --operations-only

# ---- Test & Build ----

test: ## Run all tests
	cd $(SDK_DIR) && uv run python -m pytest tests/ -v

test-unit: ## Run unit tests only
	cd $(SDK_DIR) && uv run python -m pytest tests/unit/ -v

test-integration: ## Run integration tests only
	cd $(SDK_DIR) && uv run python -m pytest tests/integration/ -v

test-cov: ## Run tests with coverage for core modules
	cd $(SDK_DIR) && uv run python -m pytest tests/ \
		--cov=workiva._auth \
		--cov=workiva._retry \
		--cov=workiva._pagination \
		--cov=workiva._client \
		--cov=workiva._errors \
		--cov=workiva.client \
		--cov=workiva.polling \
		--cov=workiva.exceptions \
		--cov-report=term-missing

build: ## Build wheel for distribution
	cd $(SDK_DIR) && uv build

publish: test build ## Publish to PyPI (set TWINE_PASSWORD or configure ~/.pypirc)
	cd $(SDK_DIR) && uv run twine upload dist/*

# ---- Cleanup ----

clean: ## Remove generated models and operations (keeps hand-written code)
	rm -f $(SDK_DIR)/src/workiva/models/platform.py
	rm -f $(SDK_DIR)/src/workiva/models/chains.py
	rm -f $(SDK_DIR)/src/workiva/models/wdata.py
	rm -f $(SDK_DIR)/src/workiva/_operations/[!_]*.py

clean-all: clean ## Remove everything including checksums
	rm -f $(CHECKSUMS_FILE)
