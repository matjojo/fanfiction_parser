import requests


def get_web_page(link, retries=5):
	page = None
	i = 1
	while i < retries:
		try:
			page = requests.get(link)
			break
		except requests.exceptions.RequestException as err:
			print(err)
			i += 1
	return page
