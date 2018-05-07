""" Site object, which handles parsing a site/game for Update posts.  """


def all_sites():
	from games.battlerite import Battlerite
	from games.leagueoflegends import LeagueOfLegends
	from games.huntshowdown import HuntShowdown
	from games.pathofexile import PathOfExile
	from games.warframe import Warframe
	from games.pubg import PUBG
	from games.fortnite import Fortnite
	from games.hearthstone import Hearthstone
	from games.csgo import CSGO
	from games.overwatch import Overwatch
	from games.dota2 import DOTA2
	from games.diablo import Diablo3
	from games.deadbydaylight import DBD
	from games.runescape import Runescape

	_sites = [Battlerite(), LeagueOfLegends(), HuntShowdown(), PathOfExile(), Warframe(), PUBG(), Fortnite(),
			Hearthstone(), CSGO(), Overwatch(), DOTA2(), Diablo3(), DBD(), Runescape()]
	return sorted(_sites, key=lambda x: x.name, reverse=False)


class Site:
	def __init__(self, name, icon=None, homepage=None):
		self.enabled = False  # Off by default.
		self.name = name
		self.icon = icon
		self._homepage = homepage

	def load(self, values):
		for k, v in values.items():
			if str(k).startswith('_') or k == 'name' or k not in vars(self):
				continue  # !cover
			setattr(self, k, v)
		#  self.__dict__.update(**values)

	def get_save_obj(self):
		ret = {}
		for k, v in vars(self).items():
			if not k.startswith('_') and k != 'name':
				ret[k] = v
		return ret

	def scan(self):
		""" Generator that should yield any Update() objects it's able to generate. """
		return []  # !cover

	def formatted_name(self, name=None):
		""" Returns this object's name, stripped of invalid characters. If provided, it formats that name instead. """
		name = name if name else self.name
		return (''.join(s for s in name.lower() if s.isalnum() or s == ' ')).title()

	def get_homepage(self):
		return self._homepage

