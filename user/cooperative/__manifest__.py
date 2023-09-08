{
    'name': 'Cooperative Volunteers',
    'summary': """Module to organize the work of their volunteers""",
    'description': """Module to managing a cooperative shop selling local products""",
        'license': 'OPL-1',
        'author': 'leandro',
        'website': 'www.cooperativeshop.com',
        'category': 'Custom Modules/Cooperative shop',
        'depends':['base'],
        'data':[
            'security/cooperative_groups.xml',
            'security/ir.model.access.csv',
            'security/cooperative_security.xml',
            'views/cooperative_menuitems.xml',
            'views/task_views.xml',
        ],
        'demo': [
            'demo/task_demo.xml',
        ],
        'application': True,
}