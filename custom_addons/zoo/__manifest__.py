{
    "name": "CHANGAN Zoo Management",
    "version": "17.0.1.0.0",
    "summary": "Zoo Management System",
    "description": """
        CHANGAN Zoo Management System
    """,
    "author": "Narupont Poolsombut",
    "license": "LGPL-3",
    "category": "Services",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/keeper_views.xml",
        "views/living_zone_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": True,
}