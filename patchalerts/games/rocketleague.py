from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from games.base_class import Site


class RocketLeague(Site):
	def __init__(self):
		super().__init__('Rocket League', icon='https://i.imgur.com/0ikRetf.png', homepage='https://www.rocketleague.com')

	def scan(self):
		soup = BeautifulSoup(
			requests.get("https://www.rocketleague.com/ajax/articles-results/?cat=7-5aa1f33-rqfqqm").text,
			"html.parser")
		#  for a in soup.find_all('a'):  #  Multiple possible, but disabled for now.
		a = soup.find('a')
		_url = 'https://www.rocketleague.com' + a['href']
		_title = a.text
		page = BeautifulSoup(requests.get(_url).text, "html.parser")
		desc = page.find(attrs={'class': ['article', 'page-content']})
		_desc = ''
		for p in desc.find_all(['li', 'strong', 'h3']):
			txt = p.text.replace('\t', '').replace('\n\n', '\n')
			if 'h' in p.name:
				txt = '**%s**' % txt
			if 'li' in p.name:
				txt = '• %s' % txt
			_desc += txt + '\n'
		yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#af6025")


if __name__ == "__main__":
	lol = RocketLeague()
	for u in lol.scan():
		print(u)
