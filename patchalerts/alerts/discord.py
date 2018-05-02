from patchalerts.classes.discord_hooks import Webhook


class Discord:
	def __init__(self, url):
		self.active = True
		self.url = url
		self.icon = 'https://i.imgur.com/rdm3W9t.png'

	def post(self, game, post_url, update_name='Click here to read more.', u_desc=None, image=None, thumb=None):
		embed = Webhook(self.url, color=123123)

		embed.set_author(name=game, icon=thumb, url=post_url)
		embed.set_title(title=update_name, url=post_url)
		embed.set_desc(u_desc.strip() if u_desc else None)
		#  embed.add_field(name='Test Field', value='Value of the field \U0001f62e')
		#  embed.add_field(name='Another Field', value='1234')
		embed.set_thumbnail(thumb)
		embed.set_image(image)
		embed.set_footer(text='Automatically generated.', icon=self.icon, ts=True)
		embed.post()


