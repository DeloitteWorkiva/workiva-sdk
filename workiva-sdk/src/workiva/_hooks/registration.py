from .types import Hooks
from .version_header import VersionHeaderHook


# This file is only ever generated once on the first generation and then is free to be modified.
# Any hooks you wish to add should be registered in the init_hooks function. Feel free to define them
# in this file or in separate files in the hooks folder.


def init_hooks(hooks: Hooks):
    hooks.register_before_request_hook(VersionHeaderHook())
