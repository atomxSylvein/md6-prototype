# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InformationSystem(models.Model):

	"""This class extends Project class and provides implements the projects statuses
	
	Attributes:
	    m_company (many2one): Company to whom the IS belongs
	    m_company_name (relative): Company name
	    m_erp_birthday (date): ERP birthday
	    m_erp_brand (str): ERP brand
	    m_erp_volume (int): not used
	    m_hypervisor_birthday (date): Hypervisor birthday
	    m_hypervisor_brand (str): Hypervisor brand
	    m_hypervisor_volume (int): Hypervisor volume
	    m_name (str): Name of the IS
	    m_server_birthday (date): Server birthday
	    m_server_brand (str): Server brand
	    m_server_volume (int): Server volume
	    m_stockage_birthday (date): Stockage birthday
	    m_stockage_brand (str): Stockage brand
	    m_stockage_volume (int): Stockage volume
	"""
	
	_name = 'si.si'
	_rec_name = 'm_name'
	_description = "Information system"

	m_name = fields.Char(compute='_compute_name', string="Nom du SI", store=True)
	m_company = fields.Many2one('res.partner', string='Société', required=True, domain="[('is_company','=',True)]")
	m_company_name = fields.Char(related='m_company.name', store=False, readonly=True)
	
	#components
	m_server_brand = fields.Char(string="Marque")
	m_server_volume = fields.Integer(string="Volume")
	m_server_birthday = fields.Date(string="Date d'anniversaire")

	m_erp_brand = fields.Char(string="Marque")
	m_erp_birthday = fields.Date(string="Date d'anniversaire")

	m_hypervisor_brand = fields.Char(string="Marque")
	m_hypervisor_volume = fields.Integer(string="Volume")
	m_hypervisor_birthday = fields.Date(string="Date d'anniversaire")

	m_stockage_brand = fields.Char(string="Marque")
	m_stockage_volume = fields.Integer(string="Volume")
	m_stockage_birthday = fields.Date(string="Date d'anniversaire")
	
	@api.depends('m_company_name')
	def _compute_name(self):
		"""Name is for example "Agrolait - SI"
		"""
		for SI in self:
			if SI.m_company_name:
				SI.m_name = ' - '.join([SI.m_company_name, 'SI'])