{
    'name': 'Odoo Goes to Space',
    'summary': """Module to try visit the Moon""",
    'description': """Module to organize the trip to the moon. This includes the spacecraft
            and space crew""",
        'license': 'OPL-1',
        'author': 'leandro',
        'website': 'www.odoo.com',
        'category': 'Custom Modules/Space',
        'depends':['base'],
        'data':[
            'security/spacemision_groups.xml',
            'security/ir.model.access.csv',
            'security/spacemision_security.xml',
            'views/spacemision_menuitems.xml',
            'views/spaceship_views.xml'
        ],
        'demo': [
            'demo/spaceship_demo.xml'
        ],
        'application': True,
}
