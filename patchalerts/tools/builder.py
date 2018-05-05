"""
	Super simple utility for updating release information.
	Be Warned: This is really bad code.
"""

import os
from sites import site_class

from util import version

if 'y' not in input('Is version: [%s] correct? (y/n): ' % version.backup_version).lower():
	raise Exception('Invalid version!')

readme = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../../README.md')

if not os.path.exists(readme):
	raise Exception('No README!')

# Really bad, really fast table replace.
out = ''
with open(readme, 'r') as r:
	tbl = False
	for line in r.readlines():
		if '| Supported Games' in line:
			tbl = True
			out += '%s\n'
		if tbl and not line.startswith('|'):
			tbl = False
		if not tbl:
			out += line
	if tbl:
		raise Exception("ERROR: Didn't reach end of supported games table. Cannot build.")


table = '|  | Supported Games |\n| ----- | ------------- |\n'
for s in site_class.all_sites():
	table += '| [<img src="%s" width="48">](%s) | [%s](%s) |\n' % (s.icon, s.get_homepage(), s.name, s.get_homepage())

out = out % table.strip()

print(table)

with open(readme, 'w') as o:
	o.write(out)

print('Built README.md')

