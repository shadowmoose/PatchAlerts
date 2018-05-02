from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from discord_hooks import Webhook

#  https://discordapp.com/developers/docs/resources/channel#embed-object-embed-author-structure
#  https://leovoel.github.io/embed-visualizer/

url = 'TODO: Loading.'


def post(game, post_url, update_name='Click here to read more.', u_desc=None, image=None, thumb=None):
	embed = Webhook(url, color=123123)

	embed.set_author(name=game, icon='https://i.imgur.com/rdm3W9t.png', url=post_url)
	embed.set_title(title=update_name, url=post_url)
	embed.set_desc(u_desc.strip() if u_desc else None)
	#  embed.add_field(name='Test Field', value='Value of the field \U0001f62e')
	#  embed.add_field(name='Another Field', value='1234')
	embed.set_thumbnail(thumb)
	embed.set_image(image)
	embed.set_footer(text='Automatically generated.', icon='https://i.imgur.com/rdm3W9t.png', ts=True)
	embed.post()


# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() + "/lib/chromedriver.exe" # TODO: Downloader, perhaps.


# Create the Chrome instance.
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("https://blog.battlerite.com/category/updates/")

elems = driver.find_elements_by_xpath("//article[@id and contains(@id, 'post-')]")
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
	post(game='Battlerite', update_name=_title, post_url=_url, u_desc=_desc, image=_img)

# capture the screen
# driver.get_screenshot_as_file("capture.png")
driver.quit()


