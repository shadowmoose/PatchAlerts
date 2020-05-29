"""
	Super simple utility for updating release information.
	Be Warned: This is really bad code.
"""


import os

from util import version
import games

if 'y' not in input('Is version: [%s] correct? (y/n): ' % version.backup_version).lower():
	raise Exception('Invalid version!')

readme = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../../README.md')

if not os.path.exists(readme):
	print(readme)
	raise Exception('No README!')

"""
# noinspection PyPackageRequirements
from PIL import Image
import requests
from io import BytesIO
os.makedirs('../../icons/', exist_ok=True)
for idx, g in enumerate(games.all_games()):
	print(g.name, g.get_icon_file_name())
	response = requests.get(g._icon)
	img = Image.open(BytesIO(response.content))
	img.thumbnail([48, 48])
	img.save('../../icons/%s' % g.get_icon_file_name())
"""

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
odd = False
for s in it:
	odd = not odd
	if not os.path.isfile('../../icons/%s' % s.get_icon_file_name()):
		raise FileNotFoundError('Missing Icon for game: %s' % os.path.abspath('../../icons/%s' % s.get_icon_file_name()))
	if odd:
		table += '| '
	table += '[![%s](%s)](%s) | [%s](%s) |' % (s.name, s.get_icon_url(), s.get_homepage(), s.name, s.get_homepage())
	if not odd:
		table += '\n'
if odd:
	table += '  |  |'
	table += '\n'

out = out % table.strip()

print(table)

with open(readme, 'w') as o:
	o.write(out)

print('Built README.md')

