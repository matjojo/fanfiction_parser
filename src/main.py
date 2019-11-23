import urllib.parse

import parsers.archive_of_our_own_org as archive_of_our_own_org
import parsers.fanfiction_net as fanfiction_net


def main():
	url = input("What ffnet or ao3 gallery to parse? (any filters in the url will be left as they are): ")
	url = "https://" + url.replace("https://", "").replace("http://", "")  # ensure the link is https
	links = []
	if "fanfiction.net" in url:
		print("fanfiction.net link detected")
		links = fanfiction_net.get_links(url)
	elif "archiveofourown.org" in url:
		print("archiveofourown.org link detected")
		url = "https://" + urllib.parse.quote(url)  # not all sites support this (ffnet grmbl)
		links = archive_of_our_own_org.get_links(url)

	with open("links.txt", "a+") as file:
		for link in links:
			file.write(link + "\n")


if __name__ == "__main__":
	main()
