# workiva

Developer-friendly & type-safe Python SDK specifically catered to leverage *workiva* API.

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=workiva&utm_campaign=python)


<!-- Start Summary [summary] -->
## Summary

Workiva API: 2026-01-01 Version of the Workiva API

For more information about the API: [Developer documentation for Workiva Inc.](https://developers.workiva.com)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [workiva](#workiva)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Pagination](#pagination)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv (recommended)

```bash
# From a local checkout
uv add /path/to/python-sdk

# From a git remote
uv add git+https://github.com/your-org/workiva-python-sdk.git
```

### PIP

```bash
pip install /path/to/python-sdk
```

### Poetry

```bash
poetry add /path/to/python-sdk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from workiva python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "workiva",
# ]
# ///

from workiva import SDK

sdk = SDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_action_by_id(activity_action_id="com.workiva.activity.retention_policy.update")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from workiva import SDK, models

async def main():

    async with SDK(
        security=models.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as sdk:

        res = await sdk.activities.get_activity_action_by_id_async(activity_action_id="com.workiva.activity.retention_policy.update")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                                            | Type   | Scheme                         |
| ----------------------------------------------- | ------ | ------------------------------ |
| `client_id`<br/>`client_secret`<br/>`token_url` | oauth2 | OAuth2 Client Credentials Flow |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_action_by_id(activity_action_id="com.workiva.activity.retention_policy.update")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Activities](docs/sdks/activities/README.md)

* [get_activity_action_by_id](docs/sdks/activities/README.md#get_activity_action_by_id) - Retrieve a single activity action
* [get_activity_actions](docs/sdks/activities/README.md#get_activity_actions) - Retrieve a list of activity actions
* [get_activity_by_id](docs/sdks/activities/README.md#get_activity_by_id) - Retrieve a single activity
* [get_organization_activities](docs/sdks/activities/README.md#get_organization_activities) - Retrieve a list of activities for an organization
* [get_organization_workspace_activities](docs/sdks/activities/README.md#get_organization_workspace_activities) - Retrieve a list of activities for a workspace

### [Admin](docs/sdks/admin/README.md)

* [assign_organization_user_roles](docs/sdks/admin/README.md#assign_organization_user_roles) - Assign roles for an Organization User
* [assign_user_to_organization](docs/sdks/admin/README.md#assign_user_to_organization) - Assign existing user to organization
* [assign_workspace_membership_roles](docs/sdks/admin/README.md#assign_workspace_membership_roles) - Assign roles for a Workspace Membership
* [create_organization_user](docs/sdks/admin/README.md#create_organization_user) - Create a new organization User
* [create_workspace](docs/sdks/admin/README.md#create_workspace) - Create a new workspace
* [create_workspace_group](docs/sdks/admin/README.md#create_workspace_group) - Create a new group in a workspace
* [create_workspace_membership](docs/sdks/admin/README.md#create_workspace_membership) - Create a new workspace membership
* [delete_organization_user_by_id](docs/sdks/admin/README.md#delete_organization_user_by_id) - Delete an organization user
* [delete_workspace_group_by_id](docs/sdks/admin/README.md#delete_workspace_group_by_id) - Delete a single group
* [delete_workspace_membership_by_id](docs/sdks/admin/README.md#delete_workspace_membership_by_id) - Delete a workspace membership
* [get_organization_by_id](docs/sdks/admin/README.md#get_organization_by_id) - Retrieve a single organization
* [get_organization_roles](docs/sdks/admin/README.md#get_organization_roles) - Retrieve available roles within an organization
* [get_organization_solutions](docs/sdks/admin/README.md#get_organization_solutions) - Retrieve available solutions within an organization
* [get_organization_user_by_id](docs/sdks/admin/README.md#get_organization_user_by_id) - Retrieve a single user in an organization
* [get_organization_user_role_list](docs/sdks/admin/README.md#get_organization_user_role_list) - List Roles assigned to an Organization User
* [get_organization_users](docs/sdks/admin/README.md#get_organization_users) - Retrieve list of an organizations users
* [get_organization_workspace_membership_roles](docs/sdks/admin/README.md#get_organization_workspace_membership_roles) - Retrieve available roles for a workspace membership
* [get_organization_workspace_roles](docs/sdks/admin/README.md#get_organization_workspace_roles) - Retrieve available roles within a workspace
* [get_organizations](docs/sdks/admin/README.md#get_organizations) - Retrieve a list of organizations
* [get_workspace_by_id](docs/sdks/admin/README.md#get_workspace_by_id) - Retrieve a single workspace
* [get_workspace_group_by_id](docs/sdks/admin/README.md#get_workspace_group_by_id) - Retrieve a single group
* [get_workspace_group_members](docs/sdks/admin/README.md#get_workspace_group_members) - Retrieve list of group members
* [get_workspace_groups](docs/sdks/admin/README.md#get_workspace_groups) - Retrieve list of groups
* [get_workspace_membership_by_id](docs/sdks/admin/README.md#get_workspace_membership_by_id) - Retrieve a single workspace membership
* [get_workspace_memberships](docs/sdks/admin/README.md#get_workspace_memberships) - Retrieve list of workspace memberships
* [get_workspace_solutions](docs/sdks/admin/README.md#get_workspace_solutions) - Retrieve available solutions within a workspace
* [get_workspace_solutions_by_id](docs/sdks/admin/README.md#get_workspace_solutions_by_id) - Retrieve a solution by id
* [get_workspaces](docs/sdks/admin/README.md#get_workspaces) - Retrieve list of workspaces
* [modify_workspace_group_members](docs/sdks/admin/README.md#modify_workspace_group_members) - Modify members in a group
* [partially_update_organization_by_id](docs/sdks/admin/README.md#partially_update_organization_by_id) - Update a single organization
* [partially_update_organization_user_by_id](docs/sdks/admin/README.md#partially_update_organization_user_by_id) - Partially update a single user in an organization
* [partially_update_workspace_by_id](docs/sdks/admin/README.md#partially_update_workspace_by_id) - Update a single workspace
* [partially_update_workspace_group_by_id](docs/sdks/admin/README.md#partially_update_workspace_group_by_id) - Update a single group
* [revoke_organization_user_roles](docs/sdks/admin/README.md#revoke_organization_user_roles) - Revoke roles for an Organization User
* [revoke_workspace_membership_roles](docs/sdks/admin/README.md#revoke_workspace_membership_roles) - Revoke roles for a Workspace Membership
* [workspace_membership_creation_with_options](docs/sdks/admin/README.md#workspace_membership_creation_with_options) - Create a new workspace membership with options

### [Chains](docs/sdks/chains/README.md)

* [chain_filter_search](docs/sdks/chains/README.md#chain_filter_search) - Search previous chain runs
* [chain_inputs_search](docs/sdks/chains/README.md#chain_inputs_search) - Search previous chain runs for an input value
* [chain_run_history](docs/sdks/chains/README.md#chain_run_history) - Return run history for a chain
* [export_chain](docs/sdks/chains/README.md#export_chain) - Export a chain
* [get_authorizations_activity](docs/sdks/chains/README.md#get_authorizations_activity) - Return a list of authorization activities
* [get_chain](docs/sdks/chains/README.md#get_chain) - Return chain properties
* [get_chain_run](docs/sdks/chains/README.md#get_chain_run) - Return chain run properties
* [get_chain_run_nodes](docs/sdks/chains/README.md#get_chain_run_nodes) - Return chain run properties with nodes
* [get_chains](docs/sdks/chains/README.md#get_chains) - Return a list of chains for an environment
* [get_commands](docs/sdks/chains/README.md#get_commands) - Return command properties
* [get_environment](docs/sdks/chains/README.md#get_environment) - Return environment properties
* [get_environments](docs/sdks/chains/README.md#get_environments) - Return a list of environments for a workspace
* [get_login_activity](docs/sdks/chains/README.md#get_login_activity) - Return a list of login activity events
* [get_permissions](docs/sdks/chains/README.md#get_permissions) - Return a list of all permissions for a company
* [get_user](docs/sdks/chains/README.md#get_user) - Return user properties
* [get_user_group](docs/sdks/chains/README.md#get_user_group) - Return user group properties
* [get_user_group_permissions](docs/sdks/chains/README.md#get_user_group_permissions) - Return a list of permissions for a user group
* [get_user_groups](docs/sdks/chains/README.md#get_user_groups) - Return a list of all user groups
* [get_user_user_groups](docs/sdks/chains/README.md#get_user_user_groups) - Return a list of user groups
* [get_users](docs/sdks/chains/README.md#get_users) - Return a list of users
* [get_workspace](docs/sdks/chains/README.md#get_workspace) - Return workspace properties
* [get_workspaces](docs/sdks/chains/README.md#get_workspaces) - Return a list of workspaces
* [import_chain](docs/sdks/chains/README.md#import_chain) - Import a chain
* [publish](docs/sdks/chains/README.md#publish) - Publish draft version of a mapping group
* [publish_chain](docs/sdks/chains/README.md#publish_chain) - Publish a chain
* [search_chains](docs/sdks/chains/README.md#search_chains) - Search chains
* [start_chain](docs/sdks/chains/README.md#start_chain) - Execute a chain
* [stop_chain](docs/sdks/chains/README.md#stop_chain) - Stop a running chain
* [update_rules](docs/sdks/chains/README.md#update_rules) - Update mapping group rules

### [Content](docs/sdks/content/README.md)

* [destination_link_source_conversion](docs/sdks/content/README.md#destination_link_source_conversion) - Initiate a destination link conversion
* [get_anchor_by_id](docs/sdks/content/README.md#get_anchor_by_id) - Retrieve an anchor by ID
* [get_column_properties](docs/sdks/content/README.md#get_column_properties) - Retrieve table column properties
* [get_destination_link_by_id](docs/sdks/content/README.md#get_destination_link_by_id) - Retrieve a destination link by id
* [get_drawing_anchor_by_id](docs/sdks/content/README.md#get_drawing_anchor_by_id) - Retrieve a drawing anchor by ID
* [get_drawing_anchor_extensions](docs/sdks/content/README.md#get_drawing_anchor_extensions) - Retrieve a list of drawing anchor extensions
* [get_drawing_anchors](docs/sdks/content/README.md#get_drawing_anchors) - Retrieve a list of drawing anchors
* [get_drawing_elements_by_id](docs/sdks/content/README.md#get_drawing_elements_by_id) - Retrieve drawing elements by id
* [get_image_by_id](docs/sdks/content/README.md#get_image_by_id) - Retrieve an image by id
* [get_range_link_by_id](docs/sdks/content/README.md#get_range_link_by_id) - Retrieve a range link by id
* [get_range_link_destinations](docs/sdks/content/README.md#get_range_link_destinations) - Retrieve range link destinations for a source
* [get_range_links](docs/sdks/content/README.md#get_range_links) - Retrieve a list of range links
* [get_rich_text_anchor_by_id](docs/sdks/content/README.md#get_rich_text_anchor_by_id) - Retrieve a rich text anchor by id
* [get_rich_text_anchor_extensions](docs/sdks/content/README.md#get_rich_text_anchor_extensions) - Retrieve a list of rich text anchor extensions
* [get_rich_text_anchors](docs/sdks/content/README.md#get_rich_text_anchors) - Retrieve a list of rich text anchors
* [get_rich_text_paragraphs](docs/sdks/content/README.md#get_rich_text_paragraphs) - Retrieve rich text paragraphs
* [get_row_properties](docs/sdks/content/README.md#get_row_properties) - Retrieve table row properties
* [get_style_guide_by_id](docs/sdks/content/README.md#get_style_guide_by_id) - Retrieve a style guide by id
* [get_table_anchor_by_id](docs/sdks/content/README.md#get_table_anchor_by_id) - Retrieve a table anchor by ID
* [get_table_anchor_extensions](docs/sdks/content/README.md#get_table_anchor_extensions) - Retrieve a list of table anchor extensions
* [get_table_anchors](docs/sdks/content/README.md#get_table_anchors) - Retrieve a list of table anchors
* [get_table_cells](docs/sdks/content/README.md#get_table_cells) - Retrieve table cell content
* [get_table_properties](docs/sdks/content/README.md#get_table_properties) - Retrieve a table's properties by id
* [image_upload](docs/sdks/content/README.md#image_upload) - Initiate upload of an image
* [partially_update_table_properties](docs/sdks/content/README.md#partially_update_table_properties) - Partially update a table's properties
* [rich_text_anchor_creation](docs/sdks/content/README.md#rich_text_anchor_creation) - Initiate creation of a new rich text anchor
* [rich_text_batch_edit](docs/sdks/content/README.md#rich_text_batch_edit) - Initiate edits to rich text
* [rich_text_duplication_edit](docs/sdks/content/README.md#rich_text_duplication_edit) - Initiate duplication edits to rich text
* [rich_text_links_batch_edit](docs/sdks/content/README.md#rich_text_links_batch_edit) - Initiate edits to rich text links
* [style_guide_export](docs/sdks/content/README.md#style_guide_export) - Initiate a style guide export
* [style_guide_import](docs/sdks/content/README.md#style_guide_import) - Initiate import of a style guide
* [table_anchor_creation](docs/sdks/content/README.md#table_anchor_creation) - Initiate creation of a new table anchor
* [table_cells_batch_edit](docs/sdks/content/README.md#table_cells_batch_edit) - Initiate edits to table cells
* [table_edit](docs/sdks/content/README.md#table_edit) - Initiate edit to a table
* [table_filters_reapplication](docs/sdks/content/README.md#table_filters_reapplication) - Reapply filters to the table
* [table_links_batch_edit](docs/sdks/content/README.md#table_links_batch_edit) - Initiate edit to table links
* [table_range_links_edit](docs/sdks/content/README.md#table_range_links_edit) - Initiate range links edits on a table

### [Documents](docs/sdks/documents/README.md)

* [copy_section](docs/sdks/documents/README.md#copy_section) - Copy section
* [create_section](docs/sdks/documents/README.md#create_section) - Create a new section in a document
* [delete_section_by_id](docs/sdks/documents/README.md#delete_section_by_id) - Delete a single section
* [document_export](docs/sdks/documents/README.md#document_export) - Initiate a document export
* [document_filters_reapplication](docs/sdks/documents/README.md#document_filters_reapplication) - Reapply filters to the document
* [document_links_publication](docs/sdks/documents/README.md#document_links_publication) - Initiate publication of links in a document
* [document_permissions_modification](docs/sdks/documents/README.md#document_permissions_modification) - Modify permissions on a document
* [edit_sections](docs/sdks/documents/README.md#edit_sections) - Initiate sections edits
* [get_document_by_id](docs/sdks/documents/README.md#get_document_by_id) - Retrieve a single document
* [get_document_milestones](docs/sdks/documents/README.md#get_document_milestones) - Retrieve a list of milestones for a document
* [get_document_permissions](docs/sdks/documents/README.md#get_document_permissions) - Retrieve permissions for a document
* [get_documents](docs/sdks/documents/README.md#get_documents) - Retrieve a list of documents
* [get_section_by_id](docs/sdks/documents/README.md#get_section_by_id) - Retrieve a single section
* [get_section_permissions](docs/sdks/documents/README.md#get_section_permissions) - Retrieve permissions for a section in a document
* [get_sections](docs/sdks/documents/README.md#get_sections) - Retrieve a list of sections
* [partially_update_document_by_id](docs/sdks/documents/README.md#partially_update_document_by_id) - Partially update a single document
* [partially_update_section_by_id](docs/sdks/documents/README.md#partially_update_section_by_id) - Partially update a single section
* [section_permissions_modification](docs/sdks/documents/README.md#section_permissions_modification) - Modify permissions on a given section of a document

### [Files](docs/sdks/files/README.md)

* [copy_file](docs/sdks/files/README.md#copy_file) - Initiate a file copy
* [create_file](docs/sdks/files/README.md#create_file) - Create a new file
* [export_file_by_id](docs/sdks/files/README.md#export_file_by_id) - Initiate a file export by ID
* [file_permissions_modification](docs/sdks/files/README.md#file_permissions_modification) - Modify permissions on a file
* [get_file_by_id](docs/sdks/files/README.md#get_file_by_id) - Retrieve a single file
* [get_file_permissions](docs/sdks/files/README.md#get_file_permissions) - Retrieve permissions for a file
* [get_files](docs/sdks/files/README.md#get_files) - Retrieve a list of files
* [get_trashed_files](docs/sdks/files/README.md#get_trashed_files) - Retrieve a list of trashed files
* [import_file](docs/sdks/files/README.md#import_file) - Initiate a file import
* [partially_update_file_by_id](docs/sdks/files/README.md#partially_update_file_by_id) - Partially update a single file
* [restore_file_by_id](docs/sdks/files/README.md#restore_file_by_id) - Initiate restoration of a single file
* [trash_file_by_id](docs/sdks/files/README.md#trash_file_by_id) - Initiate trash of a single file

### [Graph](docs/sdks/graph/README.md)

* [create_edits](docs/sdks/graph/README.md#create_edits) - Create new record edits
* [get_record_by_id](docs/sdks/graph/README.md#get_record_by_id) - Retrieve a single record
* [get_records](docs/sdks/graph/README.md#get_records) - Retrieve a list of records
* [get_type_by_id](docs/sdks/graph/README.md#get_type_by_id) - Retrieve a single type
* [get_types](docs/sdks/graph/README.md#get_types) - Retrieve a list of types
* [graph_report_export](docs/sdks/graph/README.md#graph_report_export) - Initiate a graph report export

### [Iam](docs/sdks/iam/README.md)

* [token_request](docs/sdks/iam/README.md#token_request) - Retrieve a token

### [Milestones](docs/sdks/milestones/README.md)

* [delete_milestone_by_id](docs/sdks/milestones/README.md#delete_milestone_by_id) - Deletes a milestone
* [get_milestone_by_id](docs/sdks/milestones/README.md#get_milestone_by_id) - Retrieve a milestone by id
* [milestone_creation](docs/sdks/milestones/README.md#milestone_creation) - Initiates a request to create a new milestone
* [partially_update_milestone_by_id](docs/sdks/milestones/README.md#partially_update_milestone_by_id) - Partially updates a milestone

### [Operations](docs/sdks/operations/README.md)

* [get_batch_upsertion_metric_values_results](docs/sdks/operations/README.md#get_batch_upsertion_metric_values_results) - Retrieve the results of a metric values batch upsertion operation
* [get_copy_file_results](docs/sdks/operations/README.md#get_copy_file_results) - Retrieve copy file results for a single operation
* [get_destination_link_source_conversion_results](docs/sdks/operations/README.md#get_destination_link_source_conversion_results) - Retrieves the results from a destination link source conversion.
* [get_image_upload_creation_results](docs/sdks/operations/README.md#get_image_upload_creation_results) - Retrieve results for a image upload
* [get_import_file_results](docs/sdks/operations/README.md#get_import_file_results) - Retrieve import file results for a single operation
* [get_milestone_creation_results](docs/sdks/operations/README.md#get_milestone_creation_results) - Retrieve results for a milestone creation
* [get_operation_by_id](docs/sdks/operations/README.md#get_operation_by_id) - Retrieve a single operation
* [get_patch_document_results](docs/sdks/operations/README.md#get_patch_document_results) - Retrieve results for a patch document
* [get_patch_presentation_results](docs/sdks/operations/README.md#get_patch_presentation_results) - Retrieve results for a patch presentation
* [get_patch_section_results](docs/sdks/operations/README.md#get_patch_section_results) - Retrieve results for a patch Section
* [get_patch_sheet_results](docs/sdks/operations/README.md#get_patch_sheet_results) - Retrieve results for a patch sheet
* [get_patch_slide_layout_results](docs/sdks/operations/README.md#get_patch_slide_layout_results) - Retrieve results for a patch slide layout
* [get_patch_slide_results](docs/sdks/operations/README.md#get_patch_slide_results) - Retrieve results for a patch slide
* [get_patch_spreadsheet_results](docs/sdks/operations/README.md#get_patch_spreadsheet_results) - Retrieve results for a patch spreadsheet
* [get_patch_table_properties_results](docs/sdks/operations/README.md#get_patch_table_properties_results) - Retrieve results for a patch table properties
* [get_range_link_edit_results](docs/sdks/operations/README.md#get_range_link_edit_results) - Retrieve results for a range link edit
* [get_rich_text_anchor_creation_results](docs/sdks/operations/README.md#get_rich_text_anchor_creation_results) - Retrieve results for a rich text anchor creation
* [get_rich_text_batch_edit_results](docs/sdks/operations/README.md#get_rich_text_batch_edit_results) - Retrieve results for a rich text batch edit
* [get_rich_text_duplication_edit_results](docs/sdks/operations/README.md#get_rich_text_duplication_edit_results) - Retrieve results for a rich text duplication edit
* [get_rich_text_links_batch_edit_results](docs/sdks/operations/README.md#get_rich_text_links_batch_edit_results) - Retrieve results for a rich text links batch edit
* [get_table_anchor_creation_results](docs/sdks/operations/README.md#get_table_anchor_creation_results) - Retrieve results for a table anchor creation
* [get_table_cell_edit_results](docs/sdks/operations/README.md#get_table_cell_edit_results) - Retrieve results for a table cell edit
* [get_table_edit_results](docs/sdks/operations/README.md#get_table_edit_results) - Retrieve results for a table edit
* [get_table_links_edit_results](docs/sdks/operations/README.md#get_table_links_edit_results) - Retrieve results for a table links edit
* [get_table_reapply_filter_results](docs/sdks/operations/README.md#get_table_reapply_filter_results) - Retrieve results for a table reapply filter

### [Permissions](docs/sdks/permissions/README.md)

* [get_permission_by_id](docs/sdks/permissions/README.md#get_permission_by_id) - Retrieve a single permission
* [get_permissions](docs/sdks/permissions/README.md#get_permissions) - Retrieve a list of all available permissions

### [Presentations](docs/sdks/presentations/README.md)

* [get_presentation_by_id](docs/sdks/presentations/README.md#get_presentation_by_id) - Retrieve a single presentation
* [get_presentation_milestones](docs/sdks/presentations/README.md#get_presentation_milestones) - Retrieve a list of milestones for a presentation
* [get_slide_by_id](docs/sdks/presentations/README.md#get_slide_by_id) - Retrieve a single slide
* [get_slide_layout_by_id](docs/sdks/presentations/README.md#get_slide_layout_by_id) - Retrieve a single slide layout
* [get_slide_layouts](docs/sdks/presentations/README.md#get_slide_layouts) - Retrieve a list of slide layouts
* [get_slides](docs/sdks/presentations/README.md#get_slides) - Retrieve a list of slides
* [partially_update_presentation_by_id](docs/sdks/presentations/README.md#partially_update_presentation_by_id) - Partially updates a single presentation
* [partially_update_slide_by_id](docs/sdks/presentations/README.md#partially_update_slide_by_id) - Partially update a single slide
* [partially_update_slide_layout_by_id](docs/sdks/presentations/README.md#partially_update_slide_layout_by_id) - Partially update a single slide layout
* [presentation_export](docs/sdks/presentations/README.md#presentation_export) - Initiate a presentation export
* [presentation_filters_reapplication](docs/sdks/presentations/README.md#presentation_filters_reapplication) - Reapply filters to the presentation
* [presentation_links_publication](docs/sdks/presentations/README.md#presentation_links_publication) - Initiate publication of links in a presentation

### [Reports](docs/sdks/reports/README.md)

* [get_org_report_users](docs/sdks/reports/README.md#get_org_report_users) - List organization users

### [Spreadsheets](docs/sdks/spreadsheets/README.md)

* [copy_sheet](docs/sdks/spreadsheets/README.md#copy_sheet) - Copy sheet
* [create_sheet](docs/sdks/spreadsheets/README.md#create_sheet) - Create a new sheet in a spreadsheet
* [delete_dataset_by_sheet_id](docs/sdks/spreadsheets/README.md#delete_dataset_by_sheet_id) - Delete a single dataset
* [delete_sheet_by_id](docs/sdks/spreadsheets/README.md#delete_sheet_by_id) - Delete a single sheet
* [get_datasets](docs/sdks/spreadsheets/README.md#get_datasets) - Retrieve a list of datasets
* [get_sheet_by_id](docs/sdks/spreadsheets/README.md#get_sheet_by_id) - Retrieve a single sheet
* [get_sheet_data](docs/sdks/spreadsheets/README.md#get_sheet_data) - Retrieve data from a sheet
* [get_sheet_permissions](docs/sdks/spreadsheets/README.md#get_sheet_permissions) - Retrieve permissions for a sheet in a spreadsheet
* [get_sheets](docs/sdks/spreadsheets/README.md#get_sheets) - Retrieve a list of sheets
* [get_spreadsheet_by_id](docs/sdks/spreadsheets/README.md#get_spreadsheet_by_id) - Retrieve a single spreadsheet
* [get_spreadsheet_milestones](docs/sdks/spreadsheets/README.md#get_spreadsheet_milestones) - Retrieve a list of milestones for a spreadsheet
* [get_spreadsheet_permissions](docs/sdks/spreadsheets/README.md#get_spreadsheet_permissions) - Retrieve permissions for a spreadsheet
* [get_spreadsheets](docs/sdks/spreadsheets/README.md#get_spreadsheets) - Retrieve a list of spreadsheets
* [get_values_by_range](docs/sdks/spreadsheets/README.md#get_values_by_range) - Retrieve a list of range values
* [partially_update_sheet_by_id](docs/sdks/spreadsheets/README.md#partially_update_sheet_by_id) - Partially update a single sheet
* [partially_update_spreadsheet_by_id](docs/sdks/spreadsheets/README.md#partially_update_spreadsheet_by_id) - Partially update a single spreadsheet
* [sheet_permissions_modification](docs/sdks/spreadsheets/README.md#sheet_permissions_modification) - Modify permissions on a given sheet of a spreadsheet
* [spreadsheet_export](docs/sdks/spreadsheets/README.md#spreadsheet_export) - Initiate a spreadsheet export
* [spreadsheet_filters_reapplication](docs/sdks/spreadsheets/README.md#spreadsheet_filters_reapplication) - Reapply filters to the spreadsheet
* [spreadsheet_links_publication](docs/sdks/spreadsheets/README.md#spreadsheet_links_publication) - Initiate publication of links in a spreadsheet
* [spreadsheet_permissions_modification](docs/sdks/spreadsheets/README.md#spreadsheet_permissions_modification) - Modify permissions on a spreadsheet
* [update_sheet](docs/sdks/spreadsheets/README.md#update_sheet) - Update sheet content
* [update_values_by_range](docs/sdks/spreadsheets/README.md#update_values_by_range) - Update values in a range
* [upsert_datasets](docs/sdks/spreadsheets/README.md#upsert_datasets) - Bulk upsert of datasets

### [Sustainability](docs/sdks/sustainability/README.md)

* [batch_deletion_metric_values](docs/sdks/sustainability/README.md#batch_deletion_metric_values) - Initiate a batch deletion of metric values
* [batch_upsertion_metric_values](docs/sdks/sustainability/README.md#batch_upsertion_metric_values) - Initiate a batch upsertion of metric values
* [create_dimension](docs/sdks/sustainability/README.md#create_dimension) - Create a new dimension
* [create_metric](docs/sdks/sustainability/README.md#create_metric) - Create a new metric
* [create_program](docs/sdks/sustainability/README.md#create_program) - Create a new program
* [create_topic](docs/sdks/sustainability/README.md#create_topic) - Create a new topic
* [create_value](docs/sdks/sustainability/README.md#create_value) - Create a new metric value
* [delete_metric_by_id](docs/sdks/sustainability/README.md#delete_metric_by_id) - Delete a single metric
* [delete_metric_value_by_id](docs/sdks/sustainability/README.md#delete_metric_value_by_id) - Delete a single metric value
* [delete_topic_by_id](docs/sdks/sustainability/README.md#delete_topic_by_id) - Delete a single topic
* [get_dimension_by_id](docs/sdks/sustainability/README.md#get_dimension_by_id) - Retrieve a single dimension
* [get_dimensions](docs/sdks/sustainability/README.md#get_dimensions) - Retrieve a list of dimensions
* [get_metric_by_id](docs/sdks/sustainability/README.md#get_metric_by_id) - Retrieve a single metric
* [get_metric_value_by_id](docs/sdks/sustainability/README.md#get_metric_value_by_id) - Retrieve a single metric value
* [get_metrics](docs/sdks/sustainability/README.md#get_metrics) - Retrieve a list of metrics
* [get_program_by_id](docs/sdks/sustainability/README.md#get_program_by_id) - Retrieve a single program
* [get_program_permissions](docs/sdks/sustainability/README.md#get_program_permissions) - Retrieve permissions for a program
* [get_programs](docs/sdks/sustainability/README.md#get_programs) - Retrieve a list of programs
* [get_topic_by_id](docs/sdks/sustainability/README.md#get_topic_by_id) - Retrieve a single topic
* [get_topics](docs/sdks/sustainability/README.md#get_topics) - Retrieve a list of topics
* [get_values](docs/sdks/sustainability/README.md#get_values) - Retrieve a list of metric values
* [partially_update_dimension_by_id](docs/sdks/sustainability/README.md#partially_update_dimension_by_id) - Partially update a single dimension
* [partially_update_metric_by_id](docs/sdks/sustainability/README.md#partially_update_metric_by_id) - Partially update a single metric
* [partially_update_metric_value_by_id](docs/sdks/sustainability/README.md#partially_update_metric_value_by_id) - Partially update a single metric value
* [partially_update_program_by_id](docs/sdks/sustainability/README.md#partially_update_program_by_id) - Partially update a single program
* [partially_update_topic_by_id](docs/sdks/sustainability/README.md#partially_update_topic_by_id) - Partially update a single topic
* [program_permissions_modification](docs/sdks/sustainability/README.md#program_permissions_modification) - Modify permissions on a program

### [Tasks](docs/sdks/tasks/README.md)

* [create_task](docs/sdks/tasks/README.md#create_task) - Create a new task
* [delete_task_by_id](docs/sdks/tasks/README.md#delete_task_by_id) - Delete a single task
* [get_task_by_id](docs/sdks/tasks/README.md#get_task_by_id) - Retrieve a single task
* [get_tasks](docs/sdks/tasks/README.md#get_tasks) - Retrieve a list of tasks
* [partially_update_task_by_id](docs/sdks/tasks/README.md#partially_update_task_by_id) - Partially update a single task
* [submit_task_action](docs/sdks/tasks/README.md#submit_task_action) - Initiate a task action submission

### [TestForms](docs/sdks/testforms/README.md)

* [create_matrix](docs/sdks/testforms/README.md#create_matrix) - Create a new matrix
* [create_sample](docs/sdks/testforms/README.md#create_sample) - Create a new sample
* [get_matrices](docs/sdks/testforms/README.md#get_matrices) - Retrieve a list of matrices
* [get_matrix_attachment_by_id](docs/sdks/testforms/README.md#get_matrix_attachment_by_id) - Retrieve a single matrix attachment
* [get_matrix_attachments](docs/sdks/testforms/README.md#get_matrix_attachments) - Retrieve a list of matrix attachments
* [get_matrix_by_id](docs/sdks/testforms/README.md#get_matrix_by_id) - Retrieve a single matrix
* [get_sample_attachment_by_id](docs/sdks/testforms/README.md#get_sample_attachment_by_id) - Retrieve a single sample attachment
* [get_sample_attachments](docs/sdks/testforms/README.md#get_sample_attachments) - Retrieve a list of sample attachments
* [get_sample_by_id](docs/sdks/testforms/README.md#get_sample_by_id) - Retrieve a single sample
* [get_samples](docs/sdks/testforms/README.md#get_samples) - Retrieve a list of samples
* [get_test_form_by_id](docs/sdks/testforms/README.md#get_test_form_by_id) - Retrieve a single test form
* [get_test_forms](docs/sdks/testforms/README.md#get_test_forms) - Retrieve a list of test forms
* [get_test_phase_attachment_by_id](docs/sdks/testforms/README.md#get_test_phase_attachment_by_id) - Retrieve a single test phase attachment
* [get_test_phase_attachments](docs/sdks/testforms/README.md#get_test_phase_attachments) - Retrieve a list of test phase attachments
* [get_test_phase_by_id](docs/sdks/testforms/README.md#get_test_phase_by_id) - Retrive a single test phase
* [get_test_phases](docs/sdks/testforms/README.md#get_test_phases) - Retrieve a list of test phases
* [matrix_attachment_download_by_id](docs/sdks/testforms/README.md#matrix_attachment_download_by_id) - Initiate a matrix attachment download
* [matrix_attachment_export_by_id](docs/sdks/testforms/README.md#matrix_attachment_export_by_id) - Initiate an export of a matrix attachment
* [matrix_attachment_upload](docs/sdks/testforms/README.md#matrix_attachment_upload) - Initiate a matrix attachment upload
* [partially_update_sample_by_id](docs/sdks/testforms/README.md#partially_update_sample_by_id) - Partially update a single sample
* [sample_attachment_download_by_id](docs/sdks/testforms/README.md#sample_attachment_download_by_id) - Initiate a download of a sample attachment
* [sample_attachment_export_by_id](docs/sdks/testforms/README.md#sample_attachment_export_by_id) - Initiate an export of a sample attachment
* [sample_attachment_upload](docs/sdks/testforms/README.md#sample_attachment_upload) - Initiate an upload of a sample attachment
* [sample_insertion](docs/sdks/testforms/README.md#sample_insertion) - Insert samples
* [sample_update](docs/sdks/testforms/README.md#sample_update) - Update samples
* [test_form_export](docs/sdks/testforms/README.md#test_form_export) - Initiate a test form export
* [test_phase_attachment_download_by_id](docs/sdks/testforms/README.md#test_phase_attachment_download_by_id) - Initiate a test phase attachment download
* [test_phase_attachment_export_by_id](docs/sdks/testforms/README.md#test_phase_attachment_export_by_id) - Initiate a test phase attachment export
* [test_phase_attachment_upload](docs/sdks/testforms/README.md#test_phase_attachment_upload) - Initiate a test phase attachment upload

### [Wdata](docs/sdks/wdata/README.md)

* [cancel_query](docs/sdks/wdata/README.md#cancel_query) - Cancel a running query
* [create_folder](docs/sdks/wdata/README.md#create_folder) - Create a new folder
* [create_parameter](docs/sdks/wdata/README.md#create_parameter) - Create parameter
* [create_pivot_view](docs/sdks/wdata/README.md#create_pivot_view) - Create a new pivot view
* [create_query](docs/sdks/wdata/README.md#create_query) - Create a new query
* [create_select_list](docs/sdks/wdata/README.md#create_select_list) - Create a new select list
* [create_shared_table](docs/sdks/wdata/README.md#create_shared_table) - Create a new shared table
* [create_table](docs/sdks/wdata/README.md#create_table) - Create a new table
* [create_tag](docs/sdks/wdata/README.md#create_tag) - Create a new tag
* [create_token](docs/sdks/wdata/README.md#create_token) - Create a new token
* [delete](docs/sdks/wdata/README.md#delete) - Delete a single select list
* [delete_file](docs/sdks/wdata/README.md#delete_file) - Delete a single file
* [delete_folder](docs/sdks/wdata/README.md#delete_folder) - Delete a single folder
* [delete_parameter](docs/sdks/wdata/README.md#delete_parameter) - Delete Parameter
* [delete_pivot_view](docs/sdks/wdata/README.md#delete_pivot_view) - Delete a single pivot view
* [delete_query](docs/sdks/wdata/README.md#delete_query) - Delete a single query
* [delete_shared_table](docs/sdks/wdata/README.md#delete_shared_table) - Delete a single shared table
* [delete_table](docs/sdks/wdata/README.md#delete_table) - Delete a single table
* [delete_tag](docs/sdks/wdata/README.md#delete_tag) - Delete a single tag
* [delete_workspace](docs/sdks/wdata/README.md#delete_workspace) - Delete a single workspace
* [describe_query](docs/sdks/wdata/README.md#describe_query) - List the output columns of a query
* [download_file](docs/sdks/wdata/README.md#download_file) - Download a single file
* [download_file_1](docs/sdks/wdata/README.md#download_file_1) - Download a single file
* [download_query_result](docs/sdks/wdata/README.md#download_query_result) - Download a query result
* [export_file_to_spreadsheets](docs/sdks/wdata/README.md#export_file_to_spreadsheets) - Export a file to spreadsheets
* [export_query_result_to_spreadsheets](docs/sdks/wdata/README.md#export_query_result_to_spreadsheets) - Export query result to spreadsheets
* [export_workspace](docs/sdks/wdata/README.md#export_workspace) - Export a single workspace
* [find_workspace_files_by_size](docs/sdks/wdata/README.md#find_workspace_files_by_size) - Retrieve workspace files by size
* [get_connection](docs/sdks/wdata/README.md#get_connection) - Get connection details
* [get_dependencies](docs/sdks/wdata/README.md#get_dependencies) - Retrieve dependencies
* [get_dependents](docs/sdks/wdata/README.md#get_dependents) - Retrieve a list of dependents
* [get_errors](docs/sdks/wdata/README.md#get_errors) - Retrieve errors
* [get_file](docs/sdks/wdata/README.md#get_file) - Retrieve a single file
* [get_files](docs/sdks/wdata/README.md#get_files) - Retrieve a list of files
* [get_folder](docs/sdks/wdata/README.md#get_folder) - Retrieve a single folder
* [get_import_info](docs/sdks/wdata/README.md#get_import_info) - Retrieve import information
* [get_parameter](docs/sdks/wdata/README.md#get_parameter) - Get Parameter
* [get_pivot_view](docs/sdks/wdata/README.md#get_pivot_view) - Retrieve a single pivot view
* [get_query](docs/sdks/wdata/README.md#get_query) - Retrieve a single query
* [get_query_column_data](docs/sdks/wdata/README.md#get_query_column_data) - Retrieve query column data
* [get_query_result](docs/sdks/wdata/README.md#get_query_result) - Retrieve a single query result
* [get_refresh_batch_status](docs/sdks/wdata/README.md#get_refresh_batch_status) - Gets the status of a batch refresh
* [get_refresh_status](docs/sdks/wdata/README.md#get_refresh_status) - Get connection refresh status
* [get_select_list](docs/sdks/wdata/README.md#get_select_list) - Retrieve a single select list
* [get_shared_table](docs/sdks/wdata/README.md#get_shared_table) - Retrieve a single shared table
* [get_table](docs/sdks/wdata/README.md#get_table) - Retrieve a single table
* [get_tables](docs/sdks/wdata/README.md#get_tables) - Retrieve a list of tables
* [get_tables_dependent_on_query](docs/sdks/wdata/README.md#get_tables_dependent_on_query) - Retrieve a list of dependents
* [get_workspace_query_usage](docs/sdks/wdata/README.md#get_workspace_query_usage) - Retrieve workspace query usage
* [get_workspace_upload_usage](docs/sdks/wdata/README.md#get_workspace_upload_usage) - Retrieve workspace upload usage
* [health_check](docs/sdks/wdata/README.md#health_check) - Health check
* [import_data](docs/sdks/wdata/README.md#import_data) - Import data
* [import_file](docs/sdks/wdata/README.md#import_file) - Import a single file
* [import_from_spreadsheets](docs/sdks/wdata/README.md#import_from_spreadsheets) - Import from spreadsheets
* [is_query_valid](docs/sdks/wdata/README.md#is_query_valid) - Parses the query to determine if it is valid
* [list_children](docs/sdks/wdata/README.md#list_children) - Retrieve list of folder contents
* [list_connections](docs/sdks/wdata/README.md#list_connections) - List connections
* [list_folders](docs/sdks/wdata/README.md#list_folders) - Retrieve a list of folders
* [list_parameters](docs/sdks/wdata/README.md#list_parameters) - Get Parameters
* [list_pivot_views](docs/sdks/wdata/README.md#list_pivot_views) - Retrieve a list of pivot views
* [list_queries](docs/sdks/wdata/README.md#list_queries) - Retrieve list of queries
* [list_query_results](docs/sdks/wdata/README.md#list_query_results) - Retrieve a list of query results
* [list_select_lists](docs/sdks/wdata/README.md#list_select_lists) - Retrieve a list of select lists
* [list_shared_tables](docs/sdks/wdata/README.md#list_shared_tables) - Retrieve a list of shared tables
* [list_tags](docs/sdks/wdata/README.md#list_tags) - Retrieve a list of tags
* [parse_date](docs/sdks/wdata/README.md#parse_date) - Parse a date
* [refresh_batch](docs/sdks/wdata/README.md#refresh_batch) - Refresh batch of connections
* [refresh_connection](docs/sdks/wdata/README.md#refresh_connection) - Refresh connection
* [run_query](docs/sdks/wdata/README.md#run_query) - Execute a query
* [search](docs/sdks/wdata/README.md#search) - Search
* [set_children](docs/sdks/wdata/README.md#set_children) - Move content into a folder
* [unimport_file](docs/sdks/wdata/README.md#unimport_file) - Unimport a single file
* [update_folder](docs/sdks/wdata/README.md#update_folder) - Update a single folder
* [update_parameter](docs/sdks/wdata/README.md#update_parameter) - Update Parameter
* [update_pivot_view](docs/sdks/wdata/README.md#update_pivot_view) - Update a single pivot view
* [update_query](docs/sdks/wdata/README.md#update_query) - Update a single query
* [update_select_list](docs/sdks/wdata/README.md#update_select_list) - Update a single select list
* [update_table](docs/sdks/wdata/README.md#update_table) - Update a single table
* [update_tag](docs/sdks/wdata/README.md#update_tag) - Update a single tag
* [upload_file](docs/sdks/wdata/README.md#upload_file) - Upload a single file
* [validate_filename](docs/sdks/wdata/README.md#validate_filename) - Validate whether a file with the filename can be uploaded to the table
* [validate_files](docs/sdks/wdata/README.md#validate_files) - Validate files
* [validate_tables](docs/sdks/wdata/README.md#validate_tables) - Validate tables

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_actions(dollar_maxpagesize=1000, dollar_next="JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA")

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.import_data(wipe=True)

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from workiva import SDK, models
from workiva.utils import BackoffStrategy, RetryConfig


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_action_by_id(activity_action_id="com.workiva.activity.retention_policy.update",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from workiva import SDK, models
from workiva.utils import BackoffStrategy, RetryConfig


with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_action_by_id(activity_action_id="com.workiva.activity.retention_policy.update")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SDKBaseError`](./src/workiva/errors/sdkbaseerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from workiva import SDK, errors, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:
    res = None
    try:

        res = sdk.activities.get_activity_action_by_id(activity_action_id="com.workiva.activity.retention_policy.update")

        # Handle response
        print(res)


    except errors.SDKBaseError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.ErrorResponse):
            print(e.data.code)  # Optional[str]
            print(e.data.details)  # Optional[List[models.ErrorDetails]]
            print(e.data.documentation_url)  # Optional[str]
            print(e.data.message)  # Optional[str]
            print(e.data.target)  # Optional[str]
```

### Error Classes
**Primary error:**
* [`SDKBaseError`](./src/workiva/errors/sdkbaseerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (14)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SDKBaseError`](./src/workiva/errors/sdkbaseerror.py)**:
* [`ErrorResponse`](./src/workiva/errors/errorresponse.py): Error response that indicates that the service is not able to process the incoming request. The reason is provided in the error message. Applicable to 243 of 357 methods.*
* [`SingleError`](./src/workiva/errors/singleerror.py): Applicable to 78 of 357 methods.*
* [`MultiError`](./src/workiva/errors/multierror.py): Invalid request. Status code `400`. Applicable to 34 of 357 methods.*
* [`ChainSingleError`](./src/workiva/errors/chainsingleerror.py): Applicable to 27 of 357 methods.*
* [`ErrorWithoutLineNumber`](./src/workiva/errors/errorwithoutlinenumber.py): Bad Request. Status code `400`. Applicable to 1 of 357 methods.*
* [`MappingRuleUploadResult`](./src/workiva/errors/mappingruleuploadresult.py): OK. Status code `400`. Applicable to 1 of 357 methods.*
* [`IamError`](./src/workiva/errors/iamerror.py): Error response object containing an error code. Applicable to 1 of 357 methods.*
* [`Failure`](./src/workiva/errors/failure.py): An error response. All fields other than "errors" are optional. Applicable to 1 of 357 methods.*
* [`ChainsUpdateRulesResponseBody`](./src/workiva/errors/chainsupdaterulesresponsebody.py): Unauthorized. Status code `401`. Applicable to 1 of 357 methods.*
* [`ResponseValidationError`](./src/workiva/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                       | Description |
| --- | ---------------------------- | ----------- |
| 0   | `https://api.app.wdesk.com`  | US          |
| 1   | `https://api.eu.wdesk.com`   | EU          |
| 2   | `https://api.apac.wdesk.com` | APAC        |

#### Example

```python
from workiva import SDK, models


with SDK(
    server_idx=0,
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_action_by_id(activity_action_id="com.workiva.activity.retention_policy.update")

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from workiva import SDK, models


with SDK(
    server_url="https://api.apac.wdesk.com",
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.activities.get_activity_action_by_id(activity_action_id="com.workiva.activity.retention_policy.update")

    # Handle response
    print(res)

```

### Override Server URL Per-Operation

The server URL can also be overridden on a per-operation basis, provided a server list was specified for the operation. For example:
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.wdata.cancel_query(query_result_id="<id>", server_url="https://h.apac.wdesk.com/s/wdata/prep")

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from workiva import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from workiva import SDK
from workiva.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from workiva import SDK, models
def main():

    with SDK(
        security=models.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SDK(
        security=models.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from workiva import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("workiva"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=workiva&utm_campaign=python)

## Workiva Scripting

To use this SDK from the Workiva scripting module, add it to your `requirements.txt`:

```
workiva==0.4.0
```

Then in your script:

```python
from workiva import Workiva

with Workiva(client_id="...", client_secret="...") as client:
    # List files
    response = client.files.list_files()

    # Copy a file and wait for completion
    response = client.files.copy_file(file_id="abc", file_copy=params)
    operation = client.wait(response).result(timeout=300)
```
