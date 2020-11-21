from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError


class ProductGroup(models.Model):
    _name = "product.groups"

    name = fields.Char()
    product_ids = fields.One2many('product.template', 'group_id')


class Newproduct(models.Model):
    _inherit = "product.template"

    part_number = fields.Char()
    group_id = fields.Many2one('group.id', string="group ID")
