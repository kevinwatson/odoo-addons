# -*- coding: utf-8 -*-

import pkgutil


__path__ = pkgutil.extend_path(__path__, __name__)
for _, module_name, is_package in pkgutil.walk_packages(
        path=__path__, prefix=__name__ + '.'):
    if not is_package:
        __import__(module_name)
