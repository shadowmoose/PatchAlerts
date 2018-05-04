class Alert:
	def __init__(self, name):
		self.name = name
		self.enabled = False

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

	def alert(self, upd):
		print(upd)
		return False

	def formatted_name(self, name=None):
		""" Returns this object's name, stripped of invalid characters. If provided, it formats that name instead. """
		name = name if name else self.name
		return (''.join(s for s in name.lower() if s.isalnum() or s == ' ')).title()


