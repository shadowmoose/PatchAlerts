from bs4 import BeautifulSoup
import requests
from wrappers.updates import Update


class Battlerite:
	def __init__(self):
		self.enabled = False
		self.name = 'Battlerite'

	def load(self, values):
		self.__dict__.update(**values)

	def get_save_obj(self):
		ret = {}
		for k, v in vars(self).items():
			if not k.startswith('_') and k != 'name':
				ret[k] = v
		return ret

	def scan(self):
		soup = BeautifulSoup(requests.get("https://blog.battlerite.com/category/updates/").text, "html.parser")
		elems = soup.find_all('article', id=lambda x: x and 'post' in x.lower())
		for elem in elems:
			link = elem.find('a')  # .find_element_by_xpath("//a[@href and contains(text(), 'Patch')]")
			img = elem.find('img')
			dsc = elem.find(attrs={"class": 'entry-content'})
			_url = link["href"]
			_title = link.text
			_img = img['src']
			_desc = dsc.text
			yield Update(game=self.name, update_name=_title, post_url=_url, u_desc=_desc, image=_img)

