"""
	Super simple utility for updating release information.
	Be Warned: This is really bad code.
"""

import os
import games

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


table = '|  | Supported Games | | |\n| ----- | ------------- |----- | ------------- |\n'
it = iter(games.all_games())
for s in it:
	table += '| [<img src="%s" width="48">](%s) | [%s](%s) |' % (s.icon, s.get_homepage(), s.name, s.get_homepage())
	try:
		n = next(it)
		table += ' [<img src="%s" width="48">](%s) | [%s](%s) |' % (n.icon, n.get_homepage(), n.name, n.get_homepage())
	except StopIteration:
		table += '  |  |'
	table += '\n'

out = out % table.strip()

print(table)

with open(readme, 'w') as o:
	o.write(out)

print('Built README.md')

