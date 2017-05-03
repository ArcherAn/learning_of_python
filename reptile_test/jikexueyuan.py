# _*_ coding: UTF-8 _*_

'''
本文件主要实现的是爬取极客学院总课程中所有的课程名称、简介等信息，并存入txt文件中
'''

import re
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u'开始爬取内容。。。'

    def getsource(self,url):
        html = requests.get(url)
        return html.text

    def changepage(self,url,total_page):     #实现换页功能
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []      # 定义一个列表
        for i in range(now_page,total_page+1):
            # re.sub()表示正则替换
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
            page_group.append(link)
        return page_group

    def geteveryclass(self,source):
        everyclass = re.findall('deg="0" >(.*?)</li>',source,re.S)
        return everyclass

    def getlessoninfo(self,eachclass):
        everylessoninfo = re.findall('class="lesson-infor" style="height: 88px;">(.*?</div)',eachclass,re.S)
        return everylessoninfo

    def getinfo(self,eachlessoninfo):
        info = {}
        temp = re.findall('target="_blank"(.*?)</h2>', eachlessoninfo, re.S)
        info['title'] = re.findall('>(.*?)</a>', temp[0], re.S)  #这里尤其注意temp是list格式
        info['content'] = re.findall('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>',eachlessoninfo,re.S)
        return info

    def saveinfo(self,lessoninfo):
        f = open('info.txt','a')
        for each in lessoninfo:
            f.writelines('title:' + ('').join(each['title']) + '\n')  #将'title'的list格式转为str
            f.writelines('content:' + ('').join(each['content']) + '\n')
        f.close()




if __name__ == '__main__':

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()
    all_links = jikespider.changepage(url,95)
    for link in all_links:
        print u'正在处理页面，' + link
        html = jikespider.getsource(link)
        everyclass = jikespider.geteveryclass(html)
        for each in everyclass:
            everylessoninfo = jikespider.getlessoninfo(each)
            for each1 in everylessoninfo:
                info = jikespider.getinfo(each1)
                classinfo.append(info)
    jikespider.saveinfo(classinfo)   #保存到文件中







