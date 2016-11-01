from Scraping import Scraping

if __name__ == "__main__":
	url = 'http://python.ie/pycon-2016/schedule/'
	scraping = Scraping()
	#scraping.scrapingImagesPdf(url)
	scraping.scrapingBeautifulSoup(url)