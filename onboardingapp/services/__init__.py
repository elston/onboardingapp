import os

__all__ = []

SITE_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

ignore_list = [
    '__init__.py',
    'common.py',
    'templates',
    'migrations',
    'templatetags',
    '__pycache__',
    'BaseService.py',
]

services_list = os.listdir(SITE_ROOT + "/services")
for service in services_list:
    if service not in ignore_list and ".pyc" not in service:
        service = service.replace(".py", "")
        __all__ += [service, ]
