# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017-Today Pragmatic Techsoft PVT LTD
#    (<http://www.pragtech.co.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
############################################################################
{
    'name': 'Pragmatic Property Extension',
    'version': '1.0',
    'category': 'Real Estate',
    'description': """
Extension to Pragmatic Property Management
===========================================
This module provides a rental application form and complete workflow for application approval or rejection.
     """,
    'author': 'Pragmatic Techsoft Pvt. Ltd.',
    'website': 'http://pragtech.co.in',
    'depends': ['property_management','property_booking','property_penalty','website_pms','account','project','hr_timesheet','stock','purchase','mrp'],
#     'demo': ['data/property_booking_data.xml'],
    'data': [
                'data/ir_sequence_data.xml',
                'data/schedular.xml',
                'data/email_template.xml',
                'security/ir.model.access.csv',
                'views/property_reports.xml',
                'views/rental_application_views.xml',
                'views/property_management_config.xml',
                'views/property_extension_views.xml',
                'views/account_payment_view.xml',
                'reports/property_maintenance_report.xml',
                'reports/report_rental_application_form.xml',
                'reports/property_mantanence_detail_report.xml',
                'reports/report_property_per_division.xml',
                'reports/tenant_details.xml',
                'reports/tenant_payment_report_view.xml',
                'reports/waiting_tenant_rental_application_report_view.xml',
                'wizard/property_per_division.xml',
                'wizard/tenant_daily_payment_detail_report_view.xml',
                'wizard/waiting_tenant_application_report_view.xml',
                'views/res_config_view.xml',
                'views/res_partner_extended.xml',
            ],
    'auto_install': False,
    'installable': True,
    'application': True,
    'update_xml': [],
    'demo_xml': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
