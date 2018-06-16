#!/usr/bin/python
# -*- coding: utf-8 -*-


import cgi
from jinja2 import Environment, FileSystemLoader
import cookbad_stub
import recipi
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app._static_folder = './static'

@app.route('/')
def main():
    # テンプレートファイルを指定
    env = Environment(loader=FileSystemLoader('./', encoding='shift-jis'))
    # env = Environment(loader=FileSystemLoader('./', encoding='utf-8'))
    tpl = env.get_template('./cgi-bin/template.html')

    f = cgi.FieldStorage()
    rcp, materials = cookbad_stub.web()

    materials_list = []
    for m in materials:
        materials_list.append({'name': m.name})

    after_list = []
    for a in rcp.ingredients:
        after_list.append({'name': a.name})

    steps_list = []
    for s in rcp.steps:
        steps_list.append({'dsc': s.describe})

    # html = tpl.render({'title':'aaaaa', 'materials':materials_list, 'after':after_list, 'recipi':steps_list})
    html = tpl.render({'title':'aaaaa', 'materials':materials_list, 'recipi':steps_list})
    # return render_template('./template.html', title='aaaaa', materials=materials_list, recipi=steps_list)

    #print('Content-type: text/html; charset=UTF-8\r\n')
    # print('Content-type: text/html; charset=Shift-JIS\r\n')
    return html


if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
