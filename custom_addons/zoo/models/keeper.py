from odoo import api, fields, models


class ZooKeeper(models.Model):
    _name = "zoo.keeper"
    _description = "Zoo Keeper"
    _order = "name"

    _sql_constraints = [
        (
            "positive_age",
            "CHECK(age > 0)",
            "Age must be greater than zero.",
        ),
        (
            "non_negative_salary",
            "CHECK(salary >= 0)",
            "Salary cannot be negative.",
        ),
    ]

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
        help="Name of the zoo keeper.",
    )

    position = fields.Char(
        string="Position",
        required=True,
        help="Position or responsibility of the zoo keeper.",
    )

    age = fields.Integer(
        string="Age",
        required=True,
        help="Age of the zoo keeper.",
    )

    salary = fields.Float(
        string="Monthly Salary",
        required=True,
        help="Monthly salary of the zoo keeper.",
    )

    image_1920 = fields.Image(
        string="Photo",
    )

    zone_ids = fields.One2many(
        "zoo.living.zone",
        "keeper_id",
        string="Living Zones",
    )

    zone_count = fields.Integer(
        string="Living Zones",
        compute="_compute_counts",
        store=True,
        readonly=True,
    )

    animal_count = fields.Integer(
        string="Animals",
        compute="_compute_counts",
        store=True,
        readonly=True,
    )

    @api.depends(
        "zone_ids",
        "zone_ids.animal_ids",
    )
    def _compute_counts(self):
        """Compute the number of zones and animals assigned to each keeper."""
        for keeper in self:
            zones = keeper.zone_ids
            keeper.zone_count = len(zones)
            keeper.animal_count = sum(
                len(zone.animal_ids)
                for zone in zones
            )