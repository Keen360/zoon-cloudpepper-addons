# -*- coding: utf-8 -*-
# from odoo import http


# class SprintOdooConnector(http.Controller):
#     @http.route('/sprint_odoo_connector/sprint_odoo_connector', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sprint_odoo_connector/sprint_odoo_connector/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sprint_odoo_connector.listing', {
#             'root': '/sprint_odoo_connector/sprint_odoo_connector',
#             'objects': http.request.env['sprint_odoo_connector.sprint_odoo_connector'].search([]),
#         })

#     @http.route('/sprint_odoo_connector/sprint_odoo_connector/objects/<model("sprint_odoo_connector.sprint_odoo_connector"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sprint_odoo_connector.object', {
#             'object': obj
#         })

