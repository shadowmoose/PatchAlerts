
class Update:
	def __init__(self, game, post_url, update_name=None, u_desc=None, image=None, thumb=None):
		self.game = game
		self.url = post_url.strip()
		self.name = update_name.strip() if update_name else '[Update Name]'
		self.description = u_desc.strip() if u_desc else None
		self.image = image.strip() if image else None
		self.thumb = thumb.strip() if thumb else None
		self._unsafe = {}
		"""for k, v in vars(self).items():
			if v:
				setattr(self, k, v.encode('ascii', 'replace').decode('ascii'))
		"""

	def __str__(self):
		return "Update: %s" % str(vars(self))
