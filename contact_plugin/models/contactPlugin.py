# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import informationSystem

class ContactPlugin(models.Model):

	"""This class extends Contact class and provides implements the IS & type of prospect
	
	Attributes:
	    m_prospect_type (selection): A contact can be a suspect, prospect or customer
	    m_SI (many2one): Informative System of the company
	"""
	
	_inherit = 'res.partner'
	m_prospect_type = fields.Selection([('suspect','Suspect'), ('prospect','Prospect'), ('customer','Client')], default='suspect', string="Type de contact")
	m_SI = fields.Many2one('si.si', string="Système d'information")
	customer = fields.Boolean(compute='_detect_customer', store=True)

	@api.depends('company_type')
	def _detect_customer(self):
		for contact in self:
			contact.customer = True if contact.company_type == 'company' else False
