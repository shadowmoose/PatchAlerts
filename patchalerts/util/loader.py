import requests
from bs4 import BeautifulSoup


_resp = None
latest_url = None


def _load(url, use_json=False):
	global _resp, latest_url
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
	}
	latest_url = url
	_resp = requests.get(url, headers=headers)
	if use_json:
		return _resp.json()
	else:
		return _resp.text


def direct_soup(body):
	return BeautifulSoup(body, "html.parser")


def soup(url):
	return direct_soup(_load(url))


def get_redirect():
	return _resp.url if _resp else None


def json(url):
	return _load(url, use_json=True)


