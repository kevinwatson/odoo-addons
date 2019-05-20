# -*- encoding: utf-8 -*-

{
    "name": "User Enhancements",
    "version": "0.1",
    "category": "Users",
    "description": """
    This module provides additional information about user accounts
    """,
    "author": "Kevin Watson",
    "website": "http://kevin.watson.name",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/user_permissions.xml"
    ],
    'installable': True,
    "auto_install": False,
}
