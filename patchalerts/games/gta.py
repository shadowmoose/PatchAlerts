from util import loader
from wrappers.update import Update
from games.base_class import Site


class GTA5(Site):
	def __init__(self):
		super().__init__('Grand Theft Auto 5', icon='https://i.imgur.com/MDpiySe.png',
						homepage='https://www.rockstargames.com/V/')

	def scan(self):
		dat = loader.json(
			'https://www.rockstargames.com/rockstarsupport2a/knowledge-base/get-section/115002861208.json?locale=en-us')
		articles = dat['section']['articles']
		for a in articles:
			soup = loader.direct_soup(a['body'])
			_title = a['title']
			_url = 'https://support.rockstargames.com/hc/articles/%s' % a['id']
			_desc = soup.getText('\n').strip()
			if len(_desc.split('\n')) > 1:  # Quick-n-dirty fix to remove the embedded title header.
				_desc = _desc.split('\n', 1)[1].strip()
			_desc = _desc.replace('\n\n', '\n').replace('\n\n', '\n')
			yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, thumb=self.icon, color="#588622")


if __name__ == "__main__":
	lol = GTA5()
	for u in lol.scan():
		print(u)
