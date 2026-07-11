from odoo import models, fields


class LivingZone(models.Model):
    _name = "zoo.living.zone"
    _description = "Living Zone"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    capacity = fields.Integer(string="Capacity")
    description = fields.Text(string="Description")

    keeper_id = fields.Many2one(
        "zoo.keeper",
        string="Keeper"
    )