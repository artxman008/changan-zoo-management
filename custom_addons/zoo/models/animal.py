from odoo import models, fields


class Animal(models.Model):
    _name = "zoo.animal"
    _description = "Animal"

    name = fields.Char(
        string="Name",
        required=True
    )

    species = fields.Char(
        string="Species",
        required=True
    )

    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
        required=True,
    )

    birth_date = fields.Date(
        string="Birth Date"
    )

    weight = fields.Float(
        string="Weight (kg)"
    )

    zone_id = fields.Many2one(
        "zoo.living.zone",
        string="Living Zone",
        required=True,
        ondelete="restrict",
    )