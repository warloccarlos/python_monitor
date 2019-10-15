

sms = {
		'url': 'url of the sms service you want to use',
		'payload1': 'sender_id=xxxxxxx&',
		'payload2': '&language=english&route=p&numbers=xxxxxxxxxxx',
		'headers': {
			'authorization': "dLkh6jKQoa9Gi4O2reUztVM8NRXPZ1A5EcHJ0xq7nvsCbSFyIpckV6j2C8NqTeQBgmfGYxOtwPraXz03",
			'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache"
			}
		}

access_token = {'identity_url': 'identity server url if authentication is required',
				'user': 'xxxxxxxxxxxxxxxxxxxxxx',
				'password': 'xxxxxxxxxxxxx',
				'payload': 'grant_type=password&username=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx.com&password=xxxxxxxxxxxx&scope=userinfo%20openid%20profile',
				'headers':{'use your own headers if required'}

				}

delay = {'wait':30}

api_url = {'URL KEY' : 'URL VALUE'} #For example: api_url = {'name' : 'URL of the api/resource'}
