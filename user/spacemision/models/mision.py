from odoo import api, fields, models

class Mision(models.Model):
    _name = "spacemision.mision"
    _description = "Mision Info"

    name = fields.Many2one(comodel_name="spacemision.spaceship", string='Spaceship', ondelete='cascade')
    members_crew = fields.Many2one(comodel_name="res.partner", string='Members Crew', ondelete='restrict')
    launch_date = fields.Datetime(string='Launch Date')
    return_date = fields.Datetime(string='Return Date')
    quantity_fuel = fields.Float(string="Quantity Fuel")
    miles = fields.Float(string="Miles", compute="_compute_total_miles", store = True)
    number_engine = fields.Integer(string="Numbers of motors")

    
    @api.depends("quantity_fuel")
    def _compute_total_miles(self):
        for record in self:
            record.miles = record.quantity_fuel * 3