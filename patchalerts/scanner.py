from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import traceback

from patchalerts.sites.battlerite import Battlerite
from patchalerts.alerts .discord import Discord

#  https://discordapp.com/developers/docs/resources/channel#embed-object-embed-author-structure
#  https://leovoel.github.io/embed-visualizer/

url = 'TODO: Loading.'


# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.path.abspath(os.getcwd() + "/../lib/chromedriver.exe")  # TODO: Downloader, perhaps.
print(chrome_driver)

# Create the Chrome instance.
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

# noinspection PyBroadException
try:
	dis = Discord('TODO: Load discord webhook from settings file.')
	br = Battlerite()
	br.scan(driver, dis)
except Exception as e:
	traceback.print_exc()
	pass

# capture the screen
# driver.get_screenshot_as_file("capture.png")

driver.quit()

print('Driver terminated.')
