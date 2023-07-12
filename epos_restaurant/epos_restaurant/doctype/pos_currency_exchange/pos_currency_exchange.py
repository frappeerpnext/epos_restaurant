# Copyright (c) 2023, EST Computer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class POSCurrencyExchange(Document):
	# def validate(self):
	# 	if self.from_currency == self.to_currency:
	# 		frappe.throw(_("From currency and To currency the same"));
	def on_submit(self):
		frappe.db.set_value("POS Profile", { "department": self.department }, 'exchange_rate', self.exchange_rate)