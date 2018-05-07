#!/usr/bin/env python3
import argparse
import os
import sys
import traceback
from datetime import datetime
import yaml
from util import db
from util import printing as p
from util import version
from alerts.discord import Discord
import games


parser = argparse.ArgumentParser(description="Tool for scanning Game patch notes, and relaying them to you.")
parser.add_argument("--test", help="Tells the program to check all games & exit on errors.", action="store_true")
parser.add_argument("--update", help="Update the config file and exit.", action="store_true")
parser.add_argument("--base_dir", help="Override base storage directory.", type=str, metavar='')
args = parser.parse_args()

if args.test:
	print('Running in test mode. All Games are enabled, and errors will crash the program.')

storage_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../build/')
if args.base_dir:
	storage_dir = os.path.abspath(args.base_dir.strip())  # !cover

alerts = [Discord()]
games = games.all_games()


config_file = os.path.join(storage_dir, 'config.yml')
config_backup = config_file + '.backup'
tmp_config = config_file + '.tmp'

#  error_dir = os.path.join(storage_dir, 'errors/')
os.makedirs(storage_dir, exist_ok=True)

# =======  LOAD SETTINGS  ========
config = {'alerts': {}, 'games': {}}
for cfg in [config_file, config_backup]:
	try:
		if os.path.exists(cfg):
			with open(cfg, 'r') as f:
				config = yaml.safe_load(f)
			break
	except Exception:
		continue

alert_data = config['alerts']
site_data = config['games']
out = {'games': {}, 'alerts': {}}

for a in alerts:
	for k, v in alert_data.items():
		if a.formatted_name(k) == a.formatted_name():
			a.load(v)
			print('Configured Alert: %s' % a.name)
			print('\t+Enabled: %s' % a.enabled)
	out['alerts'][a.formatted_name()] = a.get_save_obj()
print()
for s in games:
	for k, v in site_data.items():
		if s.formatted_name(k) == s.formatted_name():
			s.load(v)
			print('Configured Site: %s' % s.name)
			print('\t+Enabled: %s' % s.enabled)
	out['games'][s.formatted_name()] = s.get_save_obj()


# ACID config file saving. (Copies existing to backup, writes to temp, deletes original, renames temp). Wow.
if not os.path.exists(config_backup) and os.path.exists(config_file):
	os.rename(config_file, config_backup)
with open(tmp_config, 'w') as yaml_file:
	yaml_file.write('# Configuration file for PatchAlerts [version %s], (re)built on %s.\n' %
					(version.current_version, datetime.now().isoformat()))
	yaml.dump(out, yaml_file, default_flow_style=False, indent=4)
if os.path.exists(config_file):
	os.remove(config_file)  # !cover
os.rename(tmp_config, config_file)
if os.path.exists(config_backup):
	os.remove(config_backup)
# ======= SETTINGS APPLIED ========


db.create(os.path.join(storage_dir, 'db.sqldb'))  # Connect to (or build) the SQLite DB.

if args.update:   # !cover
	print('Update complete. Exiting.')
	sys.exit(0)


updates = []
for s in games:
	if not s.enabled and not args.test:
		continue  # !cover
	try:
		print('Scanning %s for updates...' % s.name)
		_found = False
		for u in s.scan():
			updates.append(u)
			_found = True
		if not _found:
			raise Exception('ERROR: Handler [%s] found 0 updates! Expects at least 1.' % s.name)
	except Exception:
		if args.test:
			raise
		traceback.print_exc()

print('Found %s updates.' % len(updates))

for u in updates:
	if db.check_completed(u):  # !cover
		p.out('\tAlready handled: [%s] %s' % (u.game, u.name))
		continue
	p.out('\tFound update: [%s] %s' % (u.game, u.name))
	for a in alerts:
		if a.enabled:  # !cover
			try:
				a.alert(u)
			except Exception:
				if args.test:
					raise
				traceback.print_exc()
	db.put_completed(u)

