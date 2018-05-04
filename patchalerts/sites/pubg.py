from bs4 import BeautifulSoup
import requests
from wrappers.updates import Update
from sites.site_class import Site


class PUBG(Site):
	def __init__(self):
		super().__init__("PUBG")

	def scan(self):
		soup = BeautifulSoup(requests.get("https://playbattlegrounds.com/news.pu?type_cd=2").text, "html.parser")
		table = soup.find(attrs={"id": "patchNoteList"})
		elems = table.find_all('a')
		for elem in elems:
			link = elem
			img = elem.find('img')
			dsc = elem.find(attrs={"class": 'descrption'})  # Yes, they actually spelled 'description' wrong.
			ttl = elem.find('h3')
			_url = 'https://playbattlegrounds.com' + link["href"]
			_title = ttl.text
			_img = img['src']
			_desc = dsc.text + '...'
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, image=_img, color="#bf1866")


if __name__ == "__main__":
	lol = PUBG()
	for u in lol.scan():
		print(u)
