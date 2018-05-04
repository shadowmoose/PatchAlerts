""" Site object, which handles parsing a site/game for Update posts.  """


def all_sites():
	from sites.battlerite import Battlerite
	from sites.leagueoflegends import LeagueOfLegends
	from sites.huntshowdown import HuntShowdown
	from sites.pathofexile import PathOfExile
	from sites.warframe import Warframe

	return [Battlerite(), LeagueOfLegends(), HuntShowdown(), PathOfExile(), Warframe()]


class Site:
	def __init__(self, name):
		self.enabled = True  # On by default.
		self.name = name

	def load(self, values):
		self.__dict__.update(**values)

	def get_save_obj(self):
		ret = {}
		for k, v in vars(self).items():
			if not k.startswith('_') and k != 'name':
				ret[k] = v
		return ret

	def scan(self):
		""" Generator that should yield any Update() objects it's able to generate. """
		return []

