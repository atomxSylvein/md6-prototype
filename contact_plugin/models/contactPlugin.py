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