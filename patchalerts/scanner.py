#!/usr/bin/env python3
import argparse
import os
import sys
import traceback
import yaml
from util import db
from util import printing as p

from alerts.discord import Discord
from sites import site_class


parser = argparse.ArgumentParser(description="Tool for scanning Game patch notes, and relaying them to you.")
parser.add_argument("--strict", help="Tells the program to exit on errors.", action="store_true")
parser.add_argument("--update", help="Update the config file and exit.", action="store_true")
parser.add_argument("--base_dir", help="Override base directory.", type=str, metavar='')
args = parser.parse_args()


storage_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../build/')
if args.base_dir:
	storage_dir = args.base_dir.strip()
alerts = [Discord()]
sites = site_class.all_sites()


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

if args.update:
	print('Update complete. Exiting.')
	sys.exit(0)


updates = []
for s in sites:
	if not s.enabled:
		continue
	try:
		print('Scanning %s for updates...' % s.name)
		for u in s.scan():
			updates.append(u)
	except Exception:
		if args.strict:
			raise
		traceback.print_exc()

print('Found %s updates.' % len(updates))

for u in updates:
	if db.check_completed(u):
		p.out('\tAlready handled: [%s] %s' % (u.game, u.name))
		continue
	p.out('\tFound update: [%s] %s' % (u.game, u.name))
	for a in alerts:
		if a.enabled:
			try:
				a.alert(u)
			except Exception:
				if args.strict:
					raise
				traceback.print_exc()
	db.put_completed(u)

