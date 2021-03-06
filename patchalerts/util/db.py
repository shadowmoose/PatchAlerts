import os.path
import sqlite3
import time
from contextlib import closing

conn = None


def create(file):
	global conn
	build = file == ':memory:' or not os.path.isfile(file)
	conn = sqlite3.connect(file, check_same_thread=False)
	if build:  # !cover
		with closing(conn.cursor()) as cur:
			cur.execute('''CREATE TABLE updates (
				game text, update_name text, url text, push_time numeric
			)''')
		print("Built DB.")
	print('Connected to DB.')


def check_completed(update=None, raw_url=None):
	if update:
		raw_url = update.url
	with closing(conn.cursor()) as cur:
		cur.execute('SELECT game, url FROM updates WHERE url=:ur', {'ur': raw_url})
		return cur.fetchone()


def put_completed(update):
	with closing(conn.cursor()) as cur:
		cur.execute('INSERT INTO updates (game, update_name, url, push_time) VALUES (?,?,?,?)',
														(update.game, update.name, update.url, time.time()))
		conn.commit()


def contains_game(update):
	with closing(conn.cursor()) as cur:
		cur.execute('SELECT * FROM updates WHERE game = :gm', {'gm': update.game})
		if not cur.fetchone():
			return False  # !cover
	return True
