from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import traceback
import yaml


from patchalerts.sites.battlerite import Battlerite
from patchalerts.alerts.discord import Discord


#  https://discordapp.com/developers/docs/resources/channel#embed-object-embed-author-structure
#  https://leovoel.github.io/embed-visualizer/
alerts = [Discord()]
sites = [Battlerite()]
config_file = '../config.yml'

# =======  LOAD SETTINGS  ========
with open(config_file, 'r') as f:
	config = yaml.safe_load(f)

alert_data = config['alerts']
site_data = config['sites']
out = {'sites': {}, 'alerts': {}}

for a in alerts:
	for k, v in alert_data.items():
		if k.lower() == a.name.lower():
			a.load(v)
			print('Configured Alert: %s' % a.name)
			print('\t+%s' % a.enabled)
	out['alerts'][a.name] = a.get_save_obj()

for s in sites:
	for k, v in site_data.items():
		if k.lower() == s.name.lower():
			s.load(v)
			print('Configured Site: %s' % s.name)
			print('\t+%s' % s.enabled)
	out['sites'][s.name] = s.get_save_obj()
# ======= SETTINGS APPLIED ========

with open(config_file, 'w') as yaml_file:
	yaml.dump(out, yaml_file, default_flow_style=False)

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.path.abspath(os.getcwd() + "/../lib/chromedriver.exe")  # TODO: Downloader, perhaps.
print("Using driver: %s" % chrome_driver)

# Create the Chrome instance.
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)


# noinspection PyBroadException
try:
	updates = []
	for s in sites:
		if not s.enabled:
			continue
		for u in s.scan(driver):
			updates.append(u)

	print('Found %s updates.' % len(updates))

	for u in updates:
		# TODO: Check if this update has been handled before.
		for a in alerts:
			if a.enabled:
				a.alert(u)
except Exception as e:
	traceback.print_exc()
	pass

# capture the screen
# driver.get_screenshot_as_file("capture.png")

if driver:
	driver.quit()
	print('Driver terminated.')
