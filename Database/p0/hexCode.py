import sqlite3



with sqlite3.connect('hex.sqlite3') as db:
	cur = db.cursor()

	DATA = cur.execute('''
		SELECT hex(name || age) AS X FROM Ages ORDER BY X
		''')


	for data in DATA:
		print(data)