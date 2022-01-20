# -*- coding: utf-8 -*-
# from odoo import http


# class ModuliStampaPh(http.Controller):
#     @http.route('/moduli_stampa_ph/moduli_stampa_ph/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moduli_stampa_ph/moduli_stampa_ph/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('moduli_stampa_ph.listing', {
#             'root': '/moduli_stampa_ph/moduli_stampa_ph',
#             'objects': http.request.env['moduli_stampa_ph.moduli_stampa_ph'].search([]),
#         })

#     @http.route('/moduli_stampa_ph/moduli_stampa_ph/objects/<model("moduli_stampa_ph.moduli_stampa_ph"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moduli_stampa_ph.object', {
#             'object': obj
#         })
