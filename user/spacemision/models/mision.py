from odoo import api, fields, models

class Mision(models.Model):
    _name = "spacemision.mision"
    _description = "Mision Info"

    name = fields.Many2one(comodel_name="spacemision.spaceship", string='Spaceship', ondelete='cascade')
    members_crew = fields.Many2one(comodel_name="res.partner", string='Members Crew', ondelete='restrict')
    launch_date = fields.Datetime(string='Launch Date')
    return_date = fields.Datetime(string='Return Date')