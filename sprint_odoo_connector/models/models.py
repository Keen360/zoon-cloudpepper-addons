from odoo import models, fields, _
import requests
from odoo.exceptions import UserError


class SprintConfiguration(models.Model):
    _name = 'sprint.configuration'
    _description = 'Sprint API Configuration'

    name = fields.Char(string="Configuration Name", required=True, default="Sprint API Configuration")
    create_endpoint = fields.Char(string="Create Endpoint", required=True, store=True)
    update_endpoint = fields.Char(string="Update Endpoint", required=True, store=True)
    setting_ids = fields.One2many('sprint.setting.lines', 'sprint_id', string='Setting')


class SprintConfigurationLines(models.Model):
    _name = 'sprint.setting.lines'
    _description = 'Sprint Setting Lines'

    status_code = fields.Char('Status Code')
    message = fields.Char('Message')
    partner = fields.Char('Customer')
    date_time = fields.Datetime('Date Time')
    sprint_id = fields.Many2one('sprint.configuration', string='sprint')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_code = fields.Char('Customer Code')
    sprint_customer_id = fields.Char('Sprint Customer ID')

    def sync_with_sprint(self):
        """
        Sync Odoo contacts with Sprint:
        - If `sprint_customer_id` exists, update the customer in Sprint.
        - If `sprint_customer_id` does not exist, create a new customer in Sprint.
        """
        # Fetch Sprint API configuration
        sprint_api = self.env['sprint.configuration'].search([], limit=1)
        if not sprint_api:
            raise UserError(_("Sprint API configuration not found. Please configure it in the settings."))

        for partner in self:
            # Payload for API request
            payload = {
                "name": partner.name,
                "customer_code": partner.customer_code
            }
            headers = {
                'Content-Type': 'application/json'
            }

            if partner.sprint_customer_id:
                print(partner.sprint_customer_id)
                # Update customer in Sprint
                url = sprint_api.update_endpoint.format(id=partner.sprint_customer_id)
                print(url)
                try:
                    response = requests.post(url, headers=headers, json=payload)
                    response.raise_for_status()  # Raise an error for bad HTTP responses
                except requests.RequestException as e:
                    raise UserError(_("Failed to connect to Sprint API: %s") % str(e))

                if response.status_code == 200:
                    response_data = response.json()
                    # self._log_sprint_response(sprint_api, response.status_code, response_data.get('message'))
                    partner.message_post(body=_("Contact updated in Sprint successfully."))
                else:
                    raise UserError(_("Failed to update customer in Sprint: %s") % response.text)
            else:
                # Create new customer in Sprint
                url = sprint_api.create_endpoint
                try:
                    response = requests.post(url, headers=headers, json=payload)
                    response.raise_for_status()  # Raise an error for bad HTTP responses
                except requests.RequestException as e:
                    raise UserError(_("Failed to connect to Sprint API: %s") % str(e))

                if response.status_code == 200:
                    response_data = response.json()
                    partner.sprint_customer_id = response_data.get('id')  # Save the Sprint customer ID
                    partner.customer_code = response_data.get('customer_code')
                    # self._log_sprint_response(sprint_api, response.status_code, response_data.get('message'))
                    partner.message_post(body=_("Contact created in Sprint successfully."))
                else:
                    raise UserError(_("Failed to create customer in Sprint: %s") % response.text)
            print(str(response.status_code))
            print(response_data.get('message'))
            sprint_lines = self.env['sprint.setting.lines'].create({
                'status_code': str(response.status_code),
                'message': response_data.get('message'),
                'date_time': fields.Datetime.now(),
                'partner': partner.name,
                'sprint_id': sprint_api.id  # Ensure this links the line to the correct Sprint Configuration
            })
            print(sprint_lines)
# create({
#             'template_id': sign_template.id,
#             'reference': _('Sign Request for Sale Order %s') % self.name,
#             'subject': _('Please sign the document for Sale Order %s') % self.name,
#             'request_item_ids': [(0, 0, {
