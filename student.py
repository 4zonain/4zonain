from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudRoom(models.Model):
    _name = 'stud.room'
    # _inherite=('mail.thread','mail.active.mixin')
    _description = "use it for class"


    def status_draft(self):
        for rec in self:
            rec.status ='draft'


    # @api.onchange('customer')
    # def _onchange_customer(self):
    #     if self.customer:
    #         self.company=self.customer.company_id



    @api.depends('retail_price','untaxed')
    def calc_total(self):
         for record in self:
            total = 0
            if record.retail_price:
                Total = total + record.retail_price
            if record.untaxed:
                    total = total + record.untaxed
            record.total_salary = total


 
     
    
    
    customer = fields.Many2one ('res.partner',string ="customer",required=True)
    Template = fields.Many2one('sale.order.template',string="Quotation Template")
    expiration=fields.Date(string="Expiration")
    date=fields.Datetime(string="Quotation Date")	
    Payment=fields.Many2one('account.payment.term',string="Payment Terms")
    
    teach_room_ids = fields.One2many('teach.room', 'room_id', string='Teachers')
    status =fields.Selection([('draft','Draft'),('waiting','Waiting'),('done','Done')], string="status",  readonly=True , defualt="done")
    sequence=fields.Integer(string="seq")
    
    creation=fields.Date(string="Creation Date")
    Sales=fields.Many2one('res.user',string="Sales Order")
    company=fields.Many2one('res.company',string="Company")

    total_salary=fields.Float(string="Total" , compute="calc_total")
    untaxed=fields.Float(string="untaxted amount")
    retail_price=fields.Float(string='retail price')
    image= fields.Binary(string="image")
    rate =fields.Selection([('1','very low'),('2','low'),('3','high'),('4','very high'),('5','excelent')],string="Rating")


class TeachRoom(models.Model):
    _name='teach.room'
    _description='it is for teacher'
    product_id=fields.Many2one('product.product',string='Product')
    description=fields.Text( string="Description",required=True)
    quantity=fields.Integer(string="Quantity")
    price=fields.Integer(string="Unit Price")
    taxes=fields.Many2many('account.tax',string="Taxes")
    subtotal=fields.Float(string="Subtotal", compute="calc_subtotal" )
    room_id = fields.Many2one('stud.room', string='Student Room', ondelete='cascade')

    

    @api.depends('quantity','price')
    def calc_subtotal(self):
        for rec in self:
          rec.subtotal = rec.quantity * rec.price

