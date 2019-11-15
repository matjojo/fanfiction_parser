from bs4 import BeautifulSoup

from ._parsers_util import get_web_page


def get_next_url(page):
	url = None
	try:
		for next_button in page.find_all('li', attrs={"class": "next"}):  # There are two next buttons
			# for some reason the top one sometimes doesn't have a link so we try both
			if next_button.a is not None and "Next" in next_button.a.text:
				url = "https://archiveofourown.org" + next_button.a.get('href')
				break
	except (TypeError, AttributeError) as err:
		print("ERROR: " + str(err))
		print("ERROR: The archiveofourown page structure seems to have changed, please update this parser")
		url = None
	return url


def get_story_links_in_page(page):
	urls = []
	try:
		for story_cards in page.find_all('li', attrs={"role": "article"}):
			urls.append("https://archiveofourown.org" + story_cards.div.h4.a.get("href"))
	except (TypeError, AttributeError):
		print("ERROR: The archiveofourown page structure seems to have changed, please update this parser")
	return urls


# noinspection DuplicatedCode
def get_links(url):
	links = []
	next_url = url
	while next_url is not None:
		page = get_web_page(next_url)
		if page is None:  # if for some reason the page cannot be gotten we want to at least return the links up to now
			print("Returned webpage was emtpy, are you connected to the internet?")
			return links
		print("Got page: {}".format(next_url))
		parsed_page = BeautifulSoup(page.content, 'html.parser')
		new_urls = get_story_links_in_page(parsed_page)
		print("This page added {} links".format(len(new_urls)))
		links.extend(new_urls)
		next_url = get_next_url(parsed_page)

	return links
