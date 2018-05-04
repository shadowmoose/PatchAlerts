from wrappers.discord_hooks import Webhook
from alerts.alert_class import Alert
from util import printing as p
from util import version


class Discord(Alert):
	def __init__(self):
		super().__init__('Discord')
		self.webhook = None
		self._icon = 'https://i.imgur.com/WejuXH2.png'

	def alert(self, upd):
		p.out('Discord:: Sending %s' % upd)
		embed = Webhook(self.webhook, color=upd.color)
		embed.set_author(name=upd.game, icon=upd.thumb, url=upd.url)
		embed.set_title(title=upd.name, url=upd.url)
		embed.set_desc(upd.description)
		#  embed.add_field(name='Test Field', value='Value of the field \U0001f62e')
		#  embed.add_field(name='Another Field', value='1234')
		embed.set_thumbnail(upd.thumb)
		embed.set_image(upd.image)
		embed.set_footer(text='PatchAlerts [v:%s].' % version.current_version, icon=self._icon, ts=True)
		embed.post()
		return True
