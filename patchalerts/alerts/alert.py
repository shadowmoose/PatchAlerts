class Alert:
	def __init__(self, name):
		self.name = name
		self.enabled = False

	def load(self, values):
		self.__dict__.update(**values)

	def get_save_obj(self):
		ret = {}
		for k, v in vars(self).items():
			if not k.startswith('_') and k != 'name':
				ret[k] = v
		return ret

	def alert(self, upd):
		print(upd)
		return False



