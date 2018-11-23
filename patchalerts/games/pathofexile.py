from util import loader
from wrappers.update import Update
from games.base_class import Game


class PathOfExile(Game):
	def __init__(self):
		self.alert_level = 3
		self.ignore_terms = 'sale, showcase, interview'
		super().__init__('Path of Exile', homepage='https://pathofexile.com')

	def scan(self):
		forums = [
				'https://www.pathofexile.com/forum/view-forum/366/orderby/create-time',
				'https://www.pathofexile.com/forum/view-forum/419/orderby/create-time',
				'https://www.pathofexile.com/forum/view-forum/54/orderby/create-time'
		]  # In order of importance. alert_level is a cutoff here.

		i = 0
		for forum in forums:
			i += 1
			if i > self.alert_level:
				break  # !cover
			soup = loader.soup(forum)
			table = soup.find(attrs={"class": 'viewForumTable'})
			elems = table.find('tbody').find_all('tr')
			elem = None
			for e in elems:
				# Skip to first non-sticky thread.
				if not e.find(attrs={'class': 'sticky'}):
					elem = e
					break
			ttl = elem.find(attrs={'class': 'title'})
			_title = ttl.text
			link = ttl.find('a')
			_url = 'https://www.pathofexile.com' + link["href"]
			if any(s.lower().strip() in _title.lower().strip() for s in self.ignore_terms.split(',')):
				continue  # !cover
			page = loader.soup(_url)
			dsc = page.find(attrs={'class': 'newsPost'})
			if not dsc:
				dsc = page.find(attrs={"class": 'content-container'}).find(attrs={'class': 'content'})
			_desc = dsc.getText('\n')
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#af6025")


if __name__ == "__main__":
	lol = PathOfExile()
	for u in lol.scan():
		print(u)
