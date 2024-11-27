# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Raneesha M K (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Insabhi POS',
    'version': '17.0.1.0.0',
    "category": "Theme/Backend",
    # 'summary': """Attractive and unique red-teal combination of backend-end
    #  theme for Education ERP""",
    # 'description': """In trio combination of red, teal and white Educational
    #  ERP opens the new gate way for management""",
    # 'author': 'Cybrosys Techno Solutions',
    # 'company': 'Cybrosys Techno Solutions',
    # 'maintainer': 'Cybrosys Techno Solutions',
    # 'website': "https://www.educationalerp.com",
    'depends': ['base', 'product','point_of_sale'],
    'data': [
        # 'views/products_widget.xml',
    ],
    'assets': {
    'point_of_sale._assets_pos': [
        # 'insabhi_pos/static/src/js/pos_db.js',
        # 'insabhi_pos/static/src/js/products_widget.js',
        # 'insabhi_pos/static/src/xml/products_widget.xml',
        # 'insabhi_pos/static/src/xml/product_card.xml',
    ],
    'point_of_sale.assets_prod': [
        # ('include', 'point_of_sale._assets_pos'),
        'insabhi_pos/static/src/js/product_card.js',
        'insabhi_pos/static/src/js/pos_db.js',
        'insabhi_pos/static/src/js/products_widget.js',
        'insabhi_pos/static/src/xml/products_widget.xml',
        'insabhi_pos/static/src/xml/product_card.xml',
    ],
},

     # 'web.assets_backend': [
     #     'insabhi_pos/static/src/js/product_card.js',
     #    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
