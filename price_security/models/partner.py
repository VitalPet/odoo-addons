# -*- coding: utf-8 -*-
from openerp import fields, models, api


class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.one
    def _get_user_restrict_prices(self):
        self.user_restrict_prices = self.env.user.restrict_prices

    user_restrict_prices = fields.Boolean(
        compute='_get_user_restrict_prices',
        string='User Restrict Prices')
