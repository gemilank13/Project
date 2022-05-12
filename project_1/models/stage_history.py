# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StageHistory(models.Model):
    _name = 'stage.history'
    _rec_name = 'date'
    
    date = fields.Datetime('Date')
    stage_from = fields.Many2one('stage.stage','Stage From')
    stage_to = fields.Many2one('stage.stage','Stage To')
    desc = fields.Char('Description')
    user_id = fields.Many2one('res.users', string='User', readonly=True ,default=lambda self: self.env.user)
    billing_id = fields.Many2one('billing.billing', 'Billing')
    