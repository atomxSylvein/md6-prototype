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
	customer = fields.Boolean(compute='_detect_customer', store=True)

	#IS components
	"""m_server_brand = fields.Char(string="Marque")
	m_server_volume = fields.Integer(string="Volume")
	m_server_birthday = fields.Date(string="Date d'anniversaire")

	m_erp_brand = fields.Char(string="Marque")
	m_erp_birthday = fields.Date(string="Date d'anniversaire")

	m_hypervisor_brand = fields.Char(string="Marque")
	m_hypervisor_volume = fields.Integer(string="Volume")
	m_hypervisor_birthday = fields.Date(string="Date d'anniversaire")

	m_stockage_brand = fields.Char(string="Marque")
	m_stockage_volume = fields.Integer(string="Volume")
	m_stockage_birthday = fields.Date(string="Date d'anniversaire")"""

	@api.depends('company_type')
	def _detect_customer(self):
		for contact in self:
			contact.customer = True if contact.company_type == 'company' else False
