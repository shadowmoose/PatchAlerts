""" Site object, which handles parsing a site/game for Update posts.  """


class Game:
	def __init__(self, name, homepage=None):
		self.enabled = False  # Off by default.
		self.name = name
		self._icon = self.get_icon_url()
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

	def formatted_name(self, name=None, lower=True):
		""" Returns this object's name, stripped of invalid characters. If provided, it formats that name instead. """
		name = name if name else self.name
		if lower:
			name = name.lower()
		re = (''.join(s for s in name if s.isalnum() or s == ' ')).strip()
		if lower:
			re = re.title()
		return re

	def get_homepage(self):
		return self._homepage  # !cover

	def get_icon_file_name(self):
		""" generates a file-safe name for this game's Icon file. """
		return self.formatted_name(lower=False).replace(' ', '') + '.png'

	def get_icon_url(self):
		return 'https://raw.githubusercontent.com/shadowmoose/PatchAlerts/master/icons/%s' % self.get_icon_file_name()
