from odoo import models, fields, api


class task_one(models.Model):
    _name = "task.one"

    field1 = fields.Char(string='Field1', required=True)
    field2 = fields.Char(string='Field2', compute= 'update_field2', readonly=True)
    field3 = fields.Char(string='Field3', compute= 'update_field3', readonly=True)
    
    @api.multi
    def update_field2(self):
        for rec in self:
            str = rec.field1
            list = str.split(",")
            li = []
            for i in list:
                li.append(int(i))
            only_odd = [num for num in li if num % 2 == 1]
            rec.field2 = only_odd
            
    @api.multi
    def update_field3(self):
        for rec in self:
            str = rec.field1
            list = str.split(",")
            li = []
            for i in list:
                li.append(int(i))
            res = [[li[i], li[i + 1]]
                    for i in range(len(li) - 1)]
            result = []
            for i in res:
                if sum(i) == 20:
                    result.append(i)
            rec.field3 = result