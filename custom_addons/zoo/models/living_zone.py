from odoo import api, fields, models
from odoo.exceptions import ValidationError


class LivingZone(models.Model):
    _name = "zoo.living.zone"
    _description = "Living Zone"
    _order = "code, name"

    _sql_constraints = [
        (
            "unique_zone_code",
            "unique(code)",
            "Zone code must be unique.",
        ),
        (
            "positive_capacity",
            "CHECK(capacity > 0)",
            "Capacity must be greater than zero.",
        ),
    ]

    name = fields.Char(
        string="Name", 
        required=True,
        index=True,
        help="The name of the living zone.",
    )
    
    code = fields.Char(
        string="Code",
        required=True,
        copy=False,
        index=True,
        help="Unique code of the living zone.",
    )
    
    capacity = fields.Integer(
        string="Capacity",
        required=True,
        default=1,
        help="Maximum number of animals allowed in this living zone.",
    )
    
    description = fields.Text(
        string="Description",
    )

    keeper_id = fields.Many2one(
        "zoo.keeper",
        string="Keeper",
        ondelete="restrict",
        help="The keeper responsible for this living zone.",
    )

    animal_ids = fields.One2many(
        "zoo.animal",
        "zone_id",
        string="Animals",
    )

    animal_count = fields.Integer(
        string="Animal Count",
        compute="_compute_animal_count",
        store=True,
        readonly=True,
    )

    @api.depends("animal_ids")
    def _compute_animal_count(self):
        for zone in self:
            zone.animal_count = len(zone.animal_ids)

    @api.constrains("capacity")
    def _check_capacity_against_animals(self):
        """Prevent reducing capacity below the current animal count."""
        for zone in self:
            if zone.capacity < zone.animal_count:
                raise ValidationError(
                    f"The capacity of '{zone.display_name}' cannot be lower "
                    f"than its current animal count ({zone.animal_count})."
                )

    def action_view_animals(self):
        self.ensure_one()

        action = self.env["ir.actions.actions"]._for_xml_id(
            "zoo.action_animal"
        )

        action["domain"] = [("zone_id", "=", self.id)]

        action["context"] = dict(
            self.env.context,
            default_zone_id=self.id,
        )

        return action