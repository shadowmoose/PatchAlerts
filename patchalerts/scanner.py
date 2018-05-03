#!/usr/bin/env python3

import os
import traceback
import yaml
import sys
from util import db
from util import printing as p

from alerts.discord import Discord

from sites.battlerite import Battlerite
from sites.leagueoflegends import LeagueOfLegends
from sites.huntshowdown import HuntShowdown
from sites.pathofexile import PathOfExile
from sites.warframe import Warframe


#  https://discordapp.com/developers/docs/resources/channel#embed-object-embed-author-structure
#  https://leovoel.github.io/embed-visualizer/
storage_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../build/')
alerts = [Discord()]
sites = [Battlerite(), LeagueOfLegends(), HuntShowdown(), PathOfExile(), Warframe()]


config_file = os.path.join(storage_dir, 'config.yml')
error_dir = os.path.join(storage_dir, 'errors/')

os.makedirs(error_dir, exist_ok=True)

# =======  LOAD SETTINGS  ========
config = {'alerts': {}, 'sites': {}}
if os.path.exists(config_file):
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

with open(config_file, 'w') as yaml_file:
	yaml.dump(out, yaml_file, default_flow_style=False)
# ======= SETTINGS APPLIED ========

db.create(os.path.join(storage_dir, 'db.sqldb'))


# noinspection PyBroadException

updates = []
for s in sites:
	if not s.enabled:
		continue
	# noinspection PyBroadException
	try:
		print('Scanning %s for updates...' % s.name)
		for u in s.scan():
			updates.append(u)
	except Exception as ex:
		traceback.print_exc()
		sys.exit(10)  # TODO: only with text flag.

print('Found %s updates.' % len(updates))

for u in updates:
	if db.check_completed(u):
		p.out('\tAlready handled: [%s] %s' % (u.game, u.name))
		continue
	p.out('\tFound update: [%s] %s' % (u.game, u.name))
	for a in alerts:
		if a.enabled:
			a.alert(u)
	db.put_completed(u)


# TODO: Error reporting for parsers.


