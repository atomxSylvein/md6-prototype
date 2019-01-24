# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CRMPlugin(models.Model):

	"""This class extends CRM class and provides implements the projects statuses
	
	Attributes:
	"""
	
	_inherit = 'crm.lead'
	
	#modification of existing fields
	tags_id = fields.Many2many('crm.lead.tag', string="Type de business")
	partner_id = fields.Many2one(domain="[('company_type', '=', 'company')]")
	partner_address_email = fields.Char(related='m_contact.email', string="Email", readonly=True, store=False)
	date_deadline = fields.Date(string="Date de fin de l'opportunité")
	partner_address_phone = fields.Char(related='m_contact.phone', string="Numéro de tél.", readonly=True, store=False)

	#new fields
	m_type = fields.Selection([('distribution','Distribution'), ('project','Projet')], default='distribution', string="Type d'opportunité")
	m_contact = fields.Many2one('res.partner', string="Contact de la société")
	m_lead_provider = fields.Many2one('res.partner', string="Fournisseur du lead")
	m_maturity = fields.Selection([('month', 'Dans le mois'), ('quarter', 'Dans le trimestre'), ('ahead', 'En amon de phase')], default='month', string="Maturité de l'opportunité")
	m_stage_probability = fields.Float(related='stage_id.probability', string="Probabilité", readonly=True, store=False)
	m_company_city = fields.Char(related='partner_id.city', string="Ville", store=False, readonly=True)
	m_company_zip = fields.Char(related='partner_id.zip', string="Département", store=False, readonly=True)
	m_estimated_revenue = fields.Monetary(string="Budget estimé", currency_field='company_currency')
	m_buy = fields.Monetary(string="Prix d'achat", currency_field='company_currency')
	m_sell = fields.Monetary(string="Prix de vente", currency_field='company_currency')
	m_margin = fields.Monetary(string="Marge", currency_field='company_currency', readonly=True)
	m_tjm = fields.Monetary(string="TJM", currency_field='company_currency')
	m_package_price = fields.Monetary(string="Prix forfait", currency_field='company_currency')
	