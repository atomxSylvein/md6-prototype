# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InformationSystem(models.Model):

	"""This class extends Project class and provides implements the projects statuses
	
	Attributes:
	    m_company (many2one): Company to whom the IS belongs
	    m_company_name (relative): Company name
	    m_name (str): Name of the IS
	"""
	
	_name = 'si.si'
	m_name = fields.Char(compute='_compute_name', string="Nom du SI", store=True)
	m_company = fields.Many2one('res.partner', string='Société', required=True, domain="[('is_company','=',True)]")
	m_company_name = fields.Char(related='m_company.name', store=False, readonly=True)
	
	@api.depends('m_company_name')
	def _compute_name(self):
		"""Name is for example "Agrolait - SI"
		"""
		for SI in self:
			if SI.m_company_name:
				SI.m_name = ' - '.join([SI.m_company_name, 'SI'])