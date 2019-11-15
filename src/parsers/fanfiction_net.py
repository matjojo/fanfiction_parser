from bs4 import BeautifulSoup

from ._parsers_util import get_web_page


def get_next_url(page):
	url = None
	try:
		for a in page.find_all('center')[1].find_all('a'):
			if "Next" in a.text:
				url = "https://www.fanfiction.net" + a.get('href')
				break
	except (TypeError, AttributeError):
		print("ERROR: The fanfiction.net page structure seems to have changed, please update this parser.")
		url = None
	return url


def get_story_links_in_page(page):
	urls = []
	try:
		for a in page.find_all('a', attrs={"class": "stitle"}):
			urls.append("https://www.fanfiction.net" + a.get('href'))
	except (TypeError, AttributeError):
		print("ERROR: The fanfiction.net page structure seems to have changed, please update this parser.")
	return urls


# noinspection DuplicatedCode
def get_links(url):
	links = []
	next_url = url
	while next_url is not None:
		page = get_web_page(next_url)
		print("Got page: {}".format(next_url))
		parsed_page = BeautifulSoup(page.content, 'html.parser')
		links.extend(get_story_links_in_page(parsed_page))
		next_url = get_next_url(parsed_page)

	return links
