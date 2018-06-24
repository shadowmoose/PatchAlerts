from util import loader
from wrappers.update import Update
from games.base_class import Site


class HOTS(Site):
	def __init__(self):
		super().__init__('Heroes of the Storm', icon='https://i.imgur.com/BAwhT5u.png',
						homepage='https://heroesofthestorm.com')

	def scan(self):
		soup = loader.soup("https://heroesofthestorm.com/en-us/blog/")
		cont = soup.find(attrs={'class':'news-index-section'})
		for box in cont.find_all(attrs={'class': 'news-list__item'}):
			title = box.find(attrs={'class': 'news-list__item__title'})
			desc = box.find(attrs={'class': 'news-list__item__description'})
			link = box.find('a')
			_title = title.text
			_desc = desc.get_text("\n")
			_url = link['href']
			if 'http' not in _url:
				_url = 'https://heroesofthestorm.com' + _url
			if not any(s in _title.lower() for s in ['hotfix', 'update', 'patch']):
				continue
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#632004")


if __name__ == "__main__":
	lol = HOTS()
	for u in lol.scan():
		print(u)
