{
    'name': 'Library',
    'summary': """ Module to manage books and customers""",
    'description': """Module to check out, organize and rent books""",
        'license': 'OPL-1',
        'author': 'leandro',
        'website': 'www.odoolibrary.com',
        'category': 'Custom Modules/Library',
        'depends':['base'],
        'data':[
            'security/librarypractice_groups.xml',
            'security/ir.model.access.csv',
            'security/librarypractice_security.xml',
            'views/librarypractice_menuitems.xml',
        ],
        'demo': [
            'demo/book_demo.xml',
        ],
        'application': True,
}