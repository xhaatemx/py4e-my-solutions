import sqlite3
import re

orgs = []

# create a table into sqlite Database
with sqlite3.connect('db.sqlite3') as db:
	cur = db.cursor()
	cur.execute('''
			CREATE TABLE IF NOT EXISTS organization 
			(id INTEGER AUTO INCREMENT PRIMARY KEY, org TXT, count INTEGER)
		''')

def main():
	fname = input('File Name: ')
	if len(fname) < 1: fname = 'orgs.txt'

	file = open(fname)

	for line in file:
		if not re.search('^From ', line): continue
		line = line.split()
		host = line[1].split('@')
		orgs.append(host[1])

	# start a new connection to the Database
	with sqlite3.connect('db.sqlite3') as db:
		cur = db.cursor()

		for org in orgs:
			exist = cur.execute('''
					SELECT count FROM organization WHERE org=:org
				''', {"org": org}).fetchone()

			# update count if organization is existed else set count = 1
			if exist is None:
				cur.execute('''
						INSERT INTO organization (org, count) VALUES (?, 1)
					''', (org,))
			else:
				cur.execute('''
						UPDATE organization SET count = count + 1 WHERE org = ?
					''', (org,))

	with sqlite3.connect('db.sqlite3') as db:
		cur = db.cursor()

		DATA = cur.execute('''
			SELECT org, count FROM organization ORDER BY count DESC LIMIT 10
			''')
		for row in DATA:
			print(row[0], row[1])
		cur.close()


	return 0



if __name__ == '__main__':
	main()