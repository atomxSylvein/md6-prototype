# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CRMPlugin(models.Model):

	"""This class extends CRM class and provides implements the projects statuses
	
	Attributes:
	    m_prospect_type (selection): A contact can be a suspect, prospect or customer
	    m_SI (many2one): Informative System of the company
	"""
	
	_inherit = 'crm.lead'
	m_type = fields.Selection([('distribution','Distribution'), ('project','Projet')], default='distribution', string="Type d'opportunité")
	partner_id = fields.Many2one(domain="[('company_type', '=', 'company')]")
	m_contact = fields.Many2one('res.partner', domain="[('parent_id', '=', 'partner_id')]", string="Contact de la société")
	m_maturity = fields.Selection([('month', 'Dans le mois'), ('quarter', 'Dans le trimestre'), ('ahead', 'En amon de phase')], default='month', string="Maturité de l'opportunité")
	date_deadline = fields.Date(string="Date de fin de l'opportunité")
	m_company_city = fields.Char(related='partner_id.city', string="Ville", store=False, readonly=True)
	m_company_zip = fields.Char(related='partner_id.zip', string="Département", store=False, readonly=True)
	m_estimated_revenue = fields.Monetary(string="Budget estimé", currency_field='company_currency')
	m_lead_provider = fields.Many2one('res.partner', string="Fournisseur du lead")