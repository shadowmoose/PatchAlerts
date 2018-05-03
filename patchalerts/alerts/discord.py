from wrappers.discord_hooks import Webhook
from alerts.alert_class import Alert
from util import printing as p


class Discord(Alert):
	def __init__(self):
		super().__init__('Discord')
		self.webhook = None
		self.icon = 'https://i.imgur.com/rdm3W9t.png'

	def load(self, values):
		self.__dict__.update(**values)

	def get_save_obj(self):
		ret = {}
		for k, v in vars(self).items():
			if not k.startswith('_') and k != 'name':
				ret[k] = v
		return ret

	def alert(self, upd):
		p.out('Discord:: Sending %s' % upd)
		embed = Webhook(self.webhook, color=123123)
		embed.set_author(name=upd.game, icon=upd.thumb, url=upd.url)
		embed.set_title(title=upd.name, url=upd.url)
		embed.set_desc(upd.description)
		#  embed.add_field(name='Test Field', value='Value of the field \U0001f62e')
		#  embed.add_field(name='Another Field', value='1234')
		embed.set_thumbnail(upd.thumb)
		embed.set_image(upd.image)
		embed.set_footer(text='Automatically generated.', icon=self.icon, ts=True)
		embed.post()
		return True



