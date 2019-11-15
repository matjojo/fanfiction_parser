import urllib.parse

import parsers.archive_of_our_own_org as archive_of_our_own_org
import parsers.fanfiction_net as fanfiction_net


def main():
	url = input("What ffnet or ao3 gallery to parse? (any filters in the url will be left as they are): ")
	url = url.replace("https://", "").replace("http://", "")
	url = "https://" + urllib.parse.quote(url)
	links = []
	if "fanfiction.net" in url:
		links = fanfiction_net.get_links(url)
		print("fanfiction.net link detected")
	elif "archiveofourown.org" in url:
		print("archiveofourown.org link detected")
		links = archive_of_our_own_org.get_links(url)

	with open("links.txt", "a+") as file:
		for link in links:
			file.write(link + "\n")


if __name__ == "__main__":
	main()
