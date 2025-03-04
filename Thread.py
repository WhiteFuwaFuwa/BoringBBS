import cgi
import cgitb
cgitb.enable()
import sqlite3
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.stdout.reconfigure(encoding='utf-8')

import CreatePage

t_list = []
now = os.environ.get('QUERY_STRING')
dbname = f'./db/{now}.db'
connect = sqlite3.connect(dbname)
cursor  = connect.cursor()
cursor.execute('SELECT * FROM thread')
box = cursor.fetchall()
cursor.close()
connect.close()
for i in box:
    t_list.append(i)


cp = CreatePage.CreatePage(f'ThreadPost.py?{now}')
cp.content_type()
cp.create_form(True)
cp.thread_list(t_list)
cp.page()