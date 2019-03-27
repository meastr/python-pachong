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
def getNocvelContent():
    html = urllib.request.urlopen("http://www.quanshuwang.cn/book/0/742").read()
    html = html.decode("gbk")
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'  # 利用正则表达式 匹配内容
    reg = re.compile(reg)
    urls = re.findall(reg, html)  # 这里是逗号不是点
    # 3.循环获取章节的超链接源码
    for url in urls:  # 重新循环 循环出链接   for循环
       novel_url = url[0]  # 章节的超链接
       nover_title = url[1]  # 章节标题的超链接
       chapt = urllib.request.urlopen(novel_url).read()  # 重新定义章节的链接
       chapt_html = chapt.decode("gbk")  # 进行转码
       # 4..获取小说内容
       reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'  # 正则表达式 获取 <Script>标签内的内容 就要中间正文的部分
       reg = re.compile(reg, re.S)  # S 代表 多行匹配
       chapt_content = re.findall(reg, chapt_html)  # 获取新定义的html
       chapt_content = chapt_content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;", "")  # 匹配前面的字符 替换为后面的内容
       chapt_content = chapt_content.replace("<br />", "")  # 匹配前面的字符 替换为后面的内容
       # 5.下载到本地
       print("正在保存 %s" % nover_title)
       f = open('{}.txt'.format(nover_title), 'w')
       f.write(chapt_content)

getNocvelContent()

getNovelContent()
