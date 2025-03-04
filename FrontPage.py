import cgitb
cgitb.enable()
import sys
sys.stdout.reconfigure(encoding='utf-8')
#ディレクトリの場所
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import glob
import sqlite3

import CreatePage

t_list = []
threads = glob.glob('./db/*.db')
t_number = len(threads)
if threads:
    for i in range(t_number):
        dbname  = f'./db/thread{i}.db'
        connect = sqlite3.connect(dbname)
        cursor  = connect.cursor()
        cursor.execute('SELECT * FROM thread')
        box = cursor.fetchall()
        cursor.close()
        connect.close()
        t_list.append(box[0])


cp = CreatePage.CreatePage('Post.py')
cp.content_type()
cp.create_form(True)
cp.thread_list(t_list)
cp.page()