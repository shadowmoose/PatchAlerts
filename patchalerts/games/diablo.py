from wrappers.update import Update
from games.base_class import Game
from util import loader


class Diablo3(Game):
	def __init__(self):
		super().__init__('Diablo 3', homepage='https://us.diablo3.com/en/')

	def scan(self):
		soup = loader.soup("https://us.diablo3.com/en/game/patch-notes/")
		for article in soup.find_all(attrs={'class': 'article-wrapper'}):
			anchor = article.find('a')
			url = 'https://us.diablo3.com' + anchor['href']
			title = article.find(attrs={'class': 'article-title'})
			desc = article.find(attrs={'class': 'article-summary'})
			img = 'https:' + article.find('meta', attrs={'itemprop': 'thumbnailUrl'})['content']
			_title = title.get_text(" - ")
			_desc = desc.get_text("\n")
			yield Update(game=self, update_name=_title, post_url=url, desc=_desc, color="#632004", image=img)


if __name__ == "__main__":
	lol = Diablo3()
	for u in lol.scan():
		print(u)
