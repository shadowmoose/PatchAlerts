import re


class Update:
	bold_pattern = r"\[(.+?)\]"

	def __init__(self, game, post_url, update_name, desc=None, image=None, thumb=None, color=None):
		"""
			Creates an Update wrapper object. Mostly exists just to normalize data, then transfer it to Alerters.

			:param game: The name of the Game.
			:param post_url: The URL this Update can be read at.
			:param update_name: The Title this Update was given, if it was given one.
			:param desc: The Update's summary, if it was given one.
			:param image: A link to a full-sized image for this Update, if one is available.
			:param thumb: A link to override the game thumbnail for this Update, if available.
			:param color: The color (as a Hex String) to use for this post, if the Alerter chooses to.
		"""
		self.game = game.name if game else None
		self.url = post_url.strip()
		self.name = update_name.strip().replace('\n', '').replace('\t', '') if update_name else '[Unknown Update Name]'
		self.description = desc.strip().replace('\r', '') if desc else None
		self.image = image.strip() if image else None
		self.thumb = thumb.strip() if thumb else game.get_icon_url()
		self.color = int(str(color).replace('#', ''), 16) if color else 123123
		if self.description:
			self._parse_desc()

		if not self.url or not self.url.startswith('http'):
			raise Exception('URL Error: Update URL does not exist, or is relative: [%s]' % self.url)

	def __str__(self):
		return "Update: %s" % str(vars(self))  # !cover

	def _parse_desc(self):
		self.description = self.description.replace('\r', '')
		for m in re.finditer(Update.bold_pattern, self.description):
			self.description = self.description.replace(m.group(0), '__**%s**__' % m.group(1))
		lines = self.description.split('\n')
		out = []
		last = ''
		bullets = '\t-–+*•'
		for li in lines:  # !cover
			if li.strip('.!?,'+bullets).strip() == '':
				li = ''
			if len(li.strip()) > 0 and any(li.startswith(c) for c in bullets):
				li = '• %s' % li.strip().strip(bullets)
			li = li.strip()
			if len(li) > 5 and li.lower() in self.name.lower() and last == '':
				li = ''  # Remove update title.
			if li != last:
				out.append(li)
				last = li
		self.description = '\n'.join(out[:15])
		if len(out) > 15:
			self.description += '\n...'

		if self.description and len(self.description) > 500:
			self.description = self.description[0:500].strip().rstrip('.!?•,') + '...'  # !cover
