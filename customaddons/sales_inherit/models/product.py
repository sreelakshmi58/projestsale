from odoo import api, fields, models


class CustomerOrder(models.Model):
    _name = "product.list"
    description = "product records"

    name = fields.Char(string="Product")
    currency_id = fields.Many2one("res.currency", string="Currency")
    lst_price = fields.Float(string="Price")


class SalesOrder(models.Model):
    _name = "productsale.list"
    description = "product records"


    date = fields.Date(string='Quotation Date', default=lambda s: fields.Date.context_today(s))
    customer_nameid = fields.Many2one('customer.details', string="Customer Name")
    # product_id = fields.Many2one('product.list',string="productid")
    sales_order_line_ids = fields.One2many('sales.order.line', 'reference_id')
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ], default="draft", string="status")

    price_total = fields.Float(string="Total", compute="_compute_pricetotal")

    def confirm(self):
        if not self.customer_nameid:
            raise Warning("Name should be entered")
        else:
            self.state = "confirm"

    @api.depends('sales_order_line_ids', 'sales_order_line_ids.sub_total')
    def _compute_pricetotal(self):
        for rec in self:
            total = 0.0
            for rec1 in rec.sales_order_line_ids:
                total += rec1.sub_total
            rec.price_total = total

class SalesOrder(models.Model):
    _name = "sales.order.line"
    description = "product records"

    reference_id = fields.Many2one('productsale.list',string="reference")
    product_id = fields.Many2one('product.list', string="Products")
    price = fields.Float(string="Price")
    quantity = fields.Float(string="Quantity")
    sub_total = fields.Float(string="SubTotal")




    @api.onchange('price', 'quantity')
    def _compute_price(self):
        for rec in self:
            sub_total = 0
            if rec.price and rec.quantity:
                sub_total += (rec.quantity * rec.price)
                rec.sub_total = sub_total



    # @api.onchange('product_id')
    # def _onchange_list(self):
    #     product_id = self.product_id and self.product_id.id
    #     sales_obj = self.env['product.list'].browse(product_id)
    #     self.price = sales_obj.lst_price
    @api.onchange('product_id')
    def _compute_listprice(self):
        for rec in self:
            if rec.product_id:
                rec.price = rec.product_id.lst_price




