import cgi
import cgitb
cgitb.enable()
#文字化け対策
import sys
sys.stdout.reconfigure(encoding='utf-8')
#ディレクトリの場所
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sqlite3
import bleach

import CreatePage

now = os.environ.get('QUERY_STRING')

form    = cgi.FieldStorage()
t_title = form.getvalue('t_title')
if t_title:
    t_title = bleach.clean(t_title)
text    = form.getvalue('text')
text    = bleach.clean(text)

dbname  = f'./db/{now}.db'
connect = sqlite3.connect(dbname)
cursor  = connect.cursor()
cursor.execute('INSERT INTO thread(title,text,t_number) values(?,?,?)', (t_title,text,now))
connect.commit()
cursor.close()
connect.close()

cp = CreatePage.CreatePage('')
cp.content_type()
cp.create_form(False)
cp.page()