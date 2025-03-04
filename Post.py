import cgi
import cgitb
cgitb.enable()
#文字化け対策
import sys
sys.stdout.reconfigure(encoding='utf-8')
#ディレクトリの場所
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from datetime import datetime
import glob
import sqlite3
import bleach

import CreatePage

form = cgi.FieldStorage()
t_title = form.getvalue('t_title')
t_title = bleach.clean(t_title)
text   = form.getvalue('text')
text   = bleach.clean(text)

threads = glob.glob('./db/*.db')
t_number = len(threads)
dbname = f'./db/thread{t_number}.db'
connect = sqlite3.connect(dbname)
cursor = connect.cursor()

cursor.execute('CREATE TABLE thread(rno INTEGER PRIMARY KEY AUTOINCREMENT,title STRING, text STRING, t_number STRING)')
connect.commit()
cursor.execute('INSERT INTO thread(title,text,t_number) values(?,?,?)', (t_title,text,'thread'+str(t_number)))
connect.commit()
cursor.close()
connect.close()

cp = CreatePage.CreatePage('Post.py')
cp.content_type()
cp.create_form(False)
cp.page()