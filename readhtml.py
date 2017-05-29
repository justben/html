import easygui as g
import os
import getdata


g.msgbox("请选择文件",title = 'rtk控制点报告自动读取软件', ok_button = '选择文件')
s = g.diropenbox(msg = '选择html文件所在目录：',title = 'rtk控制点报告自动读取软件')

flist = os.listdir(s)
url = []

i = 0
num = len(flist)

while i < num:
    url.append('file:///'+s+'//'+flist[i])
    i += 1

i = 0
num = len(url)

while i < num:
    getdata.getdata(url[i])
    i += 1

s = '共 读 取 html 报 告 共 计 '+str(num)+' 个 !''\n\n\n'+'2017.5.20. 测 试 版\n\n''若 在 使 用 中 发 现 问 题 ，或 者 有 改 进 建 议 ，\n随 时 联 系 郑 康 （282864241@qq） 进 行 代 码 改 进 。\n\n( 软 件 制 作： 郑  康 )'

g.codebox('完成!','rtk控制点报告自动读取软件',s)
