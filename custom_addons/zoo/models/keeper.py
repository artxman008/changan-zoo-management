from odoo import models, fields


class ZooKeeper(models.Model):
    _name = "zoo.keeper"
    _description = "Zoo Keeper"

    name = fields.Char(
        string="Name",
        required=True
    )

    position = fields.Char(
        string="Position"
    )

    age = fields.Integer(
        string="Age"
    )

    salary = fields.Float(
        string="Salary"
    )

    image = fields.Binary(
        string="Photo"
    )

    zone_ids = fields.One2many(
    "zoo.living.zone",
    "keeper_id",
    string="Living Zones"
    )