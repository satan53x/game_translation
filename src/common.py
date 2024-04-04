import json

class EnvClass:
	configPath = 'config.json'
	copyKeyToValue = False #当value为空时，复制key到value

	def loadConfig(self):
		with open(self.configPath, 'r', encoding='utf8') as f:
			data = json.loads(f.read())
			self.copyKeyToValue = data['extract']['copyKeyToValue']

Env = EnvClass()
Env.loadConfig()
