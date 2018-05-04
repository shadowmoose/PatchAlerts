from bs4 import BeautifulSoup
import requests
from wrappers.update import Update
from sites.site_class import Site


class Fortnite(Site):
	def __init__(self):
		super().__init__("Fortnite", icon='https://i.imgur.com/9Hz2BnX.png')

	def scan(self):
		resp = requests.get("https://www.epicgames.com/fortnite/en-US/patch-notes/")  # Follow redirect to latest.
		soup = BeautifulSoup(resp.text, "html.parser")
		_title = soup.find(attrs={'property': "og:title"})['content']
		_desc = soup.find(attrs={'property': "og:description"})['content']
		_img = soup.find(attrs={'property': "og:image"})['content']
		_url = resp.url
		yield Update(game=self.name, update_name=_title, post_url=_url, desc=_desc, image=_img, color="#1c237a")


if __name__ == "__main__":
	lol = Fortnite()
	for u in lol.scan():
		print(u)
