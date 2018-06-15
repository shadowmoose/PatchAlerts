from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from games.base_class import Site


class DBD(Site):
	def __init__(self):
		super().__init__('Dead By Daylight', icon='https://i.imgur.com/hL9PabV.png', homepage='http://deadbydaylight.com')

	def scan(self):
		soup = BeautifulSoup(requests.get("https://forum.deadbydaylight.com/en/categories/pc").text, "html.parser")
		announcement = soup.find(attrs={'class': 'Announcement'})
		_title = announcement.find('a').text
		link = announcement.find('a')['href']
		np = BeautifulSoup(requests.get(link).text, "html.parser")
		for li in np.find_all('li'):
			li.insert_before(soup.new_string("-"))  # Replace lists with bulletpoints.
		bod = np.find(attrs={'class': 'Item-Body'})
		_url = link
		_desc = bod.text.replace('Content - ', '')
		yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#6785c2")


if __name__ == "__main__":
	lol = DBD()
	for u in lol.scan():
		print(u)
