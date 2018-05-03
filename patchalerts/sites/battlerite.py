from patchalerts.wrappers.updates import Update


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

	def scan(self, browser):
		browser.get("https://blog.battlerite.com/category/updates/")
		elems = browser.find_elements_by_xpath("//article[@id and contains(@id, 'post-')]")
		for elem in elems:
			link = elem.find_element_by_tag_name('a')  # .find_element_by_xpath("//a[@href and contains(text(), 'Patch')]")
			img = elem.find_element_by_tag_name('img')
			dsc = elem.find_element_by_class_name('entry-content')
			_url = link.get_attribute("href")
			_title = link.text
			_img = img.get_attribute('src')
			_desc = dsc.text
			yield Update(game=self.name, update_name=_title, post_url=_url, u_desc=_desc, image=_img)

