from odoo import fields, models

class Task(models.Model):
    _name = "cooperative.task"
    _description = "Task information"

    name = fields.Char(string = "name", required=True)
    start_time = fields.Datetime(string = "start time")
    stop_time = fields.Datetime(string = "stop_time")
    occurrences = fields.Integer(default=1)
    description = fields.Text(translate=True)
    task_type = fields.Selection(string = "task type", 
                                 selection = [
                                     ("admin","Admin"),
                                     ("operative","Operative")
                                     ])
    