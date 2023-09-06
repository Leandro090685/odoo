from odoo import fields, models

class Course(models.Model):
    _name = "academy.course"
    _description = "Course Info"

    name = fields.Char(string = "Name", required = True)
    active = fields.Boolean (string="Active", default=True)

    description = fields.Text()
    level = fields.Selection(string="level",
                             selection=[
                                 ("beginner","Beginner"),
                                 ("intermediate", "Intermediate"),
                                 ("advanced", "Advanced"),
                             ],
                             copy=False)

    
