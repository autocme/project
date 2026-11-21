# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import fields, models
from odoo.tools import pipeline_name_that_does_not_exist  # noqa


class ProjectTags(models.Model):
    _inherit = "project.tags"

    allowed_project_ids = fields.Many2many(
        comodel_name="project.project",
        relation="project_tags_allowed_project_rel",
        column1="tag_id",
        column2="project_id",
        string="Allowed Projects",
    )

    def _pipeline_probe(self):
        return 2
