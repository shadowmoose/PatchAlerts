import os
import subprocess

backup_version = '1.9.0'


# Return the git revision as a string
def _git_version():
	def _minimal_ext_cmd(cmd):
		# construct minimal environment
		env = {}
		for k in ['SYSTEMROOT', 'PATH']:
			v = os.environ.get(k)
			if v is not None:
				env[k] = v
		# LANGUAGE is used on win32
		env['LANGUAGE'] = 'C'
		env['LANG'] = 'C'
		env['LC_ALL'] = 'C'
		_cwd = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
		_out = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env, cwd=_cwd, stderr=subprocess.DEVNULL).communicate()[0]
		return _out

	try:
		out = _minimal_ext_cmd(['git', 'rev-parse', '--short', 'HEAD'])
		git_revision = out.strip().decode('ascii')
		if len(git_revision) == 0:
			raise OSError()
	except OSError:
		git_revision = None
	return git_revision


def get_version():
	v = _git_version()
	if v:
		return v
	return backup_version  # !cover


# noinspection PyRedeclaration
current_version = get_version()

