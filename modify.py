#!C:\Users\xzavi\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
import sys
import _function
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

search_dir = "List/"

form = cgi.FieldStorage()
pageId = form["id"].value
context = open(search_dir + pageId,'r', encoding='utf-8').read()

try:
    title = "Modify"
    context = f"""<form action = "process_modify.py" method = "post">
    <input type="hidden" name = "title_past" value = "{pageId}">
    <p> <input type="text" name = "title" value = "{pageId}"></p>
    <p> <textarea  name = "context">{context}</textarea> </p>
    <input type="submit" onclick="return confirm('수정하시겠습니까?')">
    </form>"""
    nav_list = _function.make_list()
    _function.HTML(nav_list, "", title, context)
except Exception as e:
    print(f"""<script>
                alert("Errorcode = {e}")
                location.replace('index.py')
            </script>""")
