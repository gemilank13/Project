# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Assignment(models.Model):
    _name = 'assignment.assignment'
    
    name = fields.Char('Customer Code', required=True)
    partner_id = fields.Many2one('res.partner','Partner', required=True)
    agreement = fields.Char('Agreement', required=True)
    customer = fields.Char('Name', required=True)
    open_date = fields.Date('Open Date')
    lpd = fields.Date('LPD')
    lpa = fields.Float('LPA')
    sex = fields.Selection([('female','F'), ('male','M')], 'Sex')
    age = fields.Char('Age')
    del_del = fields.Char('DEL')
    credit_limit = fields.Float('Credit Limit (CC)')
    total_tagihan = fields.Float('Total Tagihan')
    min_payment = fields.Float('Min Payment')
    recover = fields.Float('Recover')
    angs_ke = fields.Char('Angs Ke')
    product_desc = fields.Char('Product Description')
    home_address_1 = fields.Char('Home Address 1')
    home_address_2 = fields.Char('Home Address 2')
    city = fields.Char('City')
    region = fields.Char('Region')
    zip_code = fields.Char('Zip Code')
    house_owner = fields.Char('House Ownership')
    no_hp = fields.Char('No HP', required=True)
    home_number = fields.Char('Home Number', required=True)
    birthday = fields.Date('Birthday')

    def name_get(self):
        result = [] 
        for rec in self:
            result.append((rec.id, '%s | %s | %s ' % (rec.partner_id.name, rec.name, rec.customer)))
        return result