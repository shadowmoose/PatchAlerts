
class Update:
	def __init__(self, game, post_url, update_name, desc=None, image=None, thumb=None, color=None):
		"""
			Creates an Update wrapper object. Mostly exists just to normalize data, then transfer it to Alerters.
			:param game: The name of the Game.
			:param post_url: The URL this Update can be read at.
			:param update_name: The Title this Update was given, if it was given one.
			:param desc: The Update's summary, if it was given one.
			:param image: A link to a full-sized image for this Update, if one is available.
			:param thumb: A link to a thumbnail for this Update, if available.
			:param color: The color (as a Hex String) to use for this post, if the Alerter chooses to.
		"""
		self.game = game
		self.url = post_url.strip()
		self.name = update_name.strip() if update_name else '[Unknown Update Name]'
		self.description = desc.strip() if desc else None
		self.image = image.strip() if image else None
		self.thumb = thumb.strip() if thumb else None
		self.color = int(str(color).replace('#', ''), 16) if color else 123123

		if not self.url or 'http' not in self.url:
			raise Exception('URL Error: Update URL does not exist, or is relative: [%s]' % self.url)
		"""
		self._unsafe = {}
		for k, v in vars(self).items():
			if v:
				setattr(self, k, v.encode('ascii', 'replace').decode('ascii'))
		"""

	def __str__(self):
		return "Update: %s" % str(vars(self))  # !cover
