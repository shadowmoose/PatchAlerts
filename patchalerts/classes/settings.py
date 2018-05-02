import copy


class OBJParser:
	def __init__(self, data):
		self.data = copy.deepcopy(data)
		self.default = {}
		if 'default' in self.data:
			self.default = self.data['default']
			del self.data['default']

	def parse(self):
		ret = {}
		for k, v in self.data.items():
			ob = Struct(self.default)
			ob.load(v)
			ret[k] = ob
		return ret


class Struct:
	def __init__(self, default):
		self.__dict__.update(**default)

	def load(self, values):
		self.__dict__.update(**values)



'''
test = {
	'default':{
		'default_field':'yep, here it is.'
	},
	'one':{
		'one_field':1
	},
	'two':{
		'default_field':'overruled.',
		'two_field':2
	}
}

obp = OBJParser(test)

for k,o in obp.parse().items():
	print(k,':', end='  ')
	print(o)
	for kk,vv in o.__dict__.items():
		print('\t',kk,':',vv)
#
'''