# -*- coding: utf-8 -*-

import datetime

from odoo import _, api, fields, models
from odoo.exceptions import UserError

class StockDeliveryNote(models.Model):
    _name = "stock.delivery.note"
    _inherit = "stock.delivery.note"
    
    def action_print(self):
        return self.env.ref(
            "moduli_stampa_ph.ddt_ph_report"
        ).report_action(self)

# class moduli_stampa_ph(models.Model):
#     _name = 'moduli_stampa_ph.moduli_stampa_ph'
#     _description = 'moduli_stampa_ph.moduli_stampa_ph'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
