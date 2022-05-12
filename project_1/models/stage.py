# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Stage(models.Model):
    _name = 'stage.stage'
    
    name = fields.Char('Stage Name')
    