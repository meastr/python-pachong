# !/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
import re


# 利用正则表达式

# import urllib.request.urlopen
# 1.获取主页面的源码
# 2.获取章节的超链接
# 3.获取章节的超链接源码
# 4..获取小说内容
# 5.下载到本地

# 驼峰命名法
# 小甲鱼的臀部 规定
# 注释 获取小说的内容

# 1.获取主页面的源码
def getNocvelContent():
    html = urllib.request.urlopen("http://www.quanshuwang.cn/book/154/154217").read()
    html = html.decode("gbk")
    # print(html)
    # <li><a href="http://www.quanshuwang.cn/book/0/742/238294.html" title="第一章 初临异世，共4788字">第一章 初临异世</a></li>
    # .*? 匹配所有

    # 2.获取章节的超链接

    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'  # 利用正则表达式 匹配内容
    # 目的是增加效率
    reg = re.compile(reg)
    urls = re.findall(reg, html)  # 这里是逗号不是点
    # print(urls)

    # 3.循环获取章节的超链接源码

    for url in urls:  # 重新循环 循环出链接   for循环
        # print(url)
        # 章节的超链接
        novel_url = url[0]  # 章节的超链接
        nover_title = url[1]  # 章节标题的超链接
        chapt = urllib.request.urlopen(novel_url).read()  # 重新定义章节的链接
        chapt_html = chapt.decode("gbk")  # 进行转码
        # print(chapt_html)

        # 4..获取小说内容

        reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'  # 正则表达式 获取 <Script>标签内的内容 就要中间正文的部分
        reg = re.compile(reg, re.S)  # S 代表 多行匹配
        chapt_content = re.findall(reg, chapt_html)  # 获取新定义的html
        # print(chapt_content[0])  # 列表
        # 获取小说内容
        # 替换除正文以为的其他东西
        # 替换 第一个参数   被替换的字符串       替换后的字符串   replace 替换
        chapt_content = chapt_content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;", "")  # 匹配前面的字符 替换为后面的内容
        #重新定义 为字符串
        chapt_content = chapt_content.replace("<br />", "")  # 匹配前面的字符 替换为后面的内容
        # print(chapt_content)

        # 5.下载到本地
        print("正在保存 %s"%nover_title)
        #保存  读写模式  wb
        f = open('xiaoshuo/{}.txt'.format(nover_title),'w')
        f.write(chapt_content)


getNocvelContent()
