from bs4 import BeautifulSoup
import requests
from wrappers.updates import Update
from sites.site_class import Site


class PathOfExile(Site):
	def __init__(self):
		super().__init__('Path of Exile')

	def scan(self):
		soup = BeautifulSoup(requests.get("https://www.pathofexile.com/forum/view-forum/patch-notes").text, "html.parser")
		table = soup.find(attrs={"class": 'viewForumTable'})
		elems = table.find('tbody').find_all('tr')
		for elem in elems:
			ttl = elem.find(attrs={'class': 'title'})
			link = ttl.find('a')
			dsc = elem.find(attrs={"class": 'postBy'})
			_url = 'https://www.pathofexile.com' + link["href"]
			_title = ttl.text
			_desc = dsc.text
			_thumb = 'https://i.imgur.com/4FYaeCh.png'
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=_thumb, color="#af6025")


if __name__ == "__main__":
	lol = PathOfExile()
	for u in lol.scan():
		print(u)
