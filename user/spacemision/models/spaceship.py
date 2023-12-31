from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Spaceship(models.Model):
    _name = "spacemision.spaceship"
    _description = "Spaceship Info"

    name = fields.Char(string = "name", required=True)
    active = fields.Boolean(default=True)
    type = fields.Selection(string='type', 
                            selection=[
                                ('carga', 'Carga'),
                                ('transporte', 'Transporte'),
                                ('exploracion', 'Exploracion'),
                                ('batalla', 'Batalla')
                            ], copy= False)
    model = fields.Char(string= 'model', required=True)
    build_date = fields.Date(index=True)
    captain = fields.Char(string= 'captain')
    required_crew = fields.Integer(string="required_crew")
    length = fields.Float(string='length')
    width = fields.Float(string='width')
    engine_number = fields.Char(string = 'engine_number')
    fuel_type = fields.Selection (string = 'fuel_type',
                                  selection=[
                                      ('solid_fuel', 'Solid Fuel'),
                                      ('liquid_fuel', 'Liquid Fuel')
                                  ], copy= False)
    
    @api.constrains('length', 'width')
    def _check_size(self):
        for size in self:
            if(size.width > size.length):
                raise ValidationError('The width of the spaceship cannot be greater than its length')