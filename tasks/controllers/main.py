from odoo import http
from odoo.http import request

class task_two(http.Controller):


	@http.route('/list_of_users', type='json', auth='user')
	def get_users(self):
		users_rec = request.env['res.users'].search([])
		users = []
		for rec in users_rec:
			vals = {
				'id' : rec.id,
				'name' : rec.name,
				'login' : rec.login,
				'login_date' : rec.login_date,
				'tz' : rec.login_date,
				'lang' : rec.lang
			}
			users.append(vals)
		data = {'status': 200, 'response': users, 'message': 'Success'}
		return data