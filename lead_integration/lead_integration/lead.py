import frappe
import re
import json
import traceback
import urllib
from urllib.request import urlopen
import requests

@frappe.whitelist()
def generate():
	self = frappe.get_doc("Lead Integration","IndiaMart")
	n = 0
	lead = self.indiamart_url.format(frappe.utils.get_url())
	res = requests.post(url=lead)
	req = json.loads(res.text)
	leads = req.items()
	for key,value in leads:
		if key == 'MESSAGE' and value != "":
			pass
		else:
			if key == 'TOTAL_RECORDS':
				n = value
			for i in range(0, n):
				if key == 'RESPONSE':
					if not frappe.db.exists("Lead",{"india_mart_id":lead_data["QUERY_ID"]}):
						id = value[i]["UNIQUE_QUERY_ID"]
						name = value[i]["SENDER_NAME"]
						time = value[i]["QUERY_TIME"]
						mobile = value[i]["SENDER_MOBILE"]
						email = value[i]["SENDER_EMAIL"]
						company = value[i]["SENDER_COMPANY"]
						address = value[i]["SENDER_ADDRESS"]
						city = value[i]["SENDER_CITY"]
						state = value[i]["SENDER_STATE"]
						iso = value[i]["SENDER_COUNTRY_ISO"]
						product_name = value[i]["QUERY_PRODUCT_NAME"]
						message = value[i]["QUERY_MESSAGE"]
						doc = frappe.get_doc(dict(
							doctype="Lead",
							lead_name=name,
							email_address=email,
							phone=mobile,
							requirement=product_name,
							india_mart_id=id,
							source="India Mart",
							notes=message,
							company_name=company,
							city=city,
							state=state,
							country=iso     
						)).insert(ignore_permissions = True)
						



def add_lead(lead_data):
	try:
		if not frappe.db.exists("Lead",{"india_mart_id":lead_data["QUERY_ID"]}):
			doc = frappe.get_doc(dict(
				doctype="Lead",
				lead_name=lead_data["SENDERNAME"],
				email_address=lead_data["SENDEREMAIL"],
				phone=lead_data["MOB"],
				requirement=lead_data["SUBJECT"],
				india_mart_id=lead_data["QUERY_ID"],
				source="India Mart"           
			)).insert(ignore_permissions = True)
			return doc
	except Exception as e:
		frappe.log_error(frappe.get_traceback())