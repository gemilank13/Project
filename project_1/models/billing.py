# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Billing(models.Model):
    _name = 'billing.billing'
    
    name = fields.Char(string="Billing Code", readonly=True, required=True, copy=False, default='New')
    cust_code_id = fields.Many2one('assignment.assignment','Customer Code', required=True)
    user_id = fields.Many2one('res.users', string='User', readonly=True ,default=lambda self: self.env.user)
    stage_history_ids = fields.One2many('stage.history', 'billing_id', string="Stage History")


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('self.billing') or 'New'
        result = super(Billing, self).create(vals)
        return result