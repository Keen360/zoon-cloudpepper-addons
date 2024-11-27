from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    x_studio_consignee = fields.Many2one(
        'res.partner',
        string='Customer',
        related='product_tmpl_id.x_studio_consignee',
        store=True,
    )
