

class Battlerite:
	def __init__(self):
		self.enabled = True
		self.name = 'Battlerite'

	def scan(self, browser, alert):
		browser.get("https://blog.battlerite.com/category/updates/")
		elems = browser.find_elements_by_xpath("//article[@id and contains(@id, 'post-')]")
		for elem in elems:
			link = elem.find_element_by_tag_name('a')  # .find_element_by_xpath("//a[@href and contains(text(), 'Patch')]")
			img = elem.find_element_by_tag_name('img')
			dsc = elem.find_element_by_class_name('entry-content')
			print(link.get_attribute("href"))
			print(img.get_attribute('src'))
			print('[%s]' % elem.text)
			_url = link.get_attribute("href")
			_title = link.text
			_img = img.get_attribute('src')
			_desc = dsc.text
			alert.post(game=self.name, update_name=_title, post_url=_url, u_desc=_desc, image=_img)

