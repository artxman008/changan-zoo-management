from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Animal(models.Model):
    _name = "zoo.animal"
    _description = "Animal"
    _order = "name, species"

    _sql_constraints = [
        (
            "positive_weight",
            "CHECK(weight > 0)",
            "Weight must be greater than zero.",
        ),
    ]

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
        help="Name used to identify the animal.",
    )

    species = fields.Char(
        string="Species",
        required=True,
        index=True,
        help="Species of the animal, such as Lion, Tiger, or Elephant.",
    )

    gender = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
        required=True,
    )

    birth_date = fields.Date(
        string="Birth Date",
        help="Birth date of the animal.",
    )

    weight = fields.Float(
        string="Weight (kg)",
        required=True,
        help="Current weight of the animal in kilograms.",
    )

    zone_id = fields.Many2one(
        comodel_name="zoo.living.zone",
        string="Living Zone",
        required=True,
        index=True,
        ondelete="restrict",
        help="Living zone assigned to this animal.",
    )

    @api.constrains("zone_id")
    def _check_zone_capacity(self):
        """Prevent assigning animals to a zone beyond its capacity."""
        for animal in self.filtered("zone_id"):
            zone = animal.zone_id

            if zone.animal_count > zone.capacity:
                raise ValidationError(
                    f"The living zone '{zone.display_name}' "
                    "has reached its maximum capacity."
                )

    @api.constrains("birth_date")
    def _check_birth_date(self):
        """Prevent entering a birth date in the future."""
        today = fields.Date.context_today(self)

        for animal in self.filtered("birth_date"):
            if animal.birth_date > today:
                raise ValidationError(
                    "Birth date cannot be in the future."
                )