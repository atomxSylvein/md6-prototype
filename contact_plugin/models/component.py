# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Component(models.Model):

	"""This class is for the IS components
	
	Attributes:
	    m_birthday (date): Birthday of the component
	    m_brand (str): Component's brand
	    m_type (selection): Components can be servers, erp, etc.
	    m_volume (int): Volume of the component
	"""
	
	_name = 'si.component'
	m_type = fields.Selection([("server","Serveur"), ("erp","ERP"), ("hypervisor", "Hyperviseur"), ("stock", "Stockage")], string="Élément du SI", required=True)
	m_brand = fields.Char(string="Marque")
	m_volume = fields.Integer(string="Volume")
	m_birthday = fields.Date(string="Date d'anniversaire")

	