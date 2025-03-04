class CreatePage:
    def __init__(self, action):
        self.action = action
        self.threads = ''
        self.pin = ''
    def content_type(self):
        return print("Content-Type: text/html\n")
    def create_form(self,form):
            if form == True:
                self.form = f'''<div>
        <form action = "{self.action}" method = "POST">
            <div><input type = "text" name = "t_title"></div>
            <div><textarea name = "text"></textarea><div>
            <div><input type = "submit" value= "投稿"></div>
        </form>
        </div>
'''
            else:
                 self.form = ''
    def thread_list(self,threads):
         for i in threads:
            if i[1] == None:
                self.threads += f'<div><a href="Thread.py?{i[3]}">{i[0]}</a></div><div>{i[2]}</div>'
            else:
                self.threads += f'<div><a href="Thread.py?{i[3]}">{i[0]}</a></div><div>{i[1]}</div><div>{i[2]}</div>'

    def page(self):
        html = f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>ふつうの掲示板</title>
    </head>
    <body>
    <div><a href="FrontPage.py">トップ</a></div>
    {self.form}
    {self.threads}
    </body>
</html>
'''
        return print(html)