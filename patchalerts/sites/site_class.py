""" Site object, which handles parsing a site/game for Update posts.  """


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

