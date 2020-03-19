from util import loader
from wrappers.update import Update
from games.base_class import Game


class HOTS(Game):
	def __init__(self):
		super().__init__('Heroes of the Storm', homepage='https://heroesofthestorm.com')

	def scan(self):
		encoded = loader.json('https://news.blizzard.com/en-us/blog/list?pageNum=1&pageSize=30&community=heroes-of-the-storm')
		soup = loader.direct_soup(encoded['html'])
		elems = soup.find_all(attrs={'class': 'ArticleListItem'})
		for elem in elems:
			a = elem.find('a')
			dsc = elem.find(attrs={"class": 'ArticleListItem-description'})
			title = elem.find(attrs={'class': 'ArticleListItem-title'})
			_url = 'https://news.blizzard.com/' + a['href']
			_title = title.text
			_desc = dsc.text
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color="#632004")


if __name__ == "__main__":
	lol = HOTS()
	for u in lol.scan():
		print(u)
