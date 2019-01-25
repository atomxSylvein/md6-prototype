# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CRMTagPlugin(models.Model):

	"""This class extends CRM Tag class and provides a tag type
	
	Attributes:
	"""
	
	_inherit = 'crm.lead.tag'
	m_type = fields.Selection([('distribution','Distribution'), ('project','Projet')], default='distribution', string="Type de business")
	