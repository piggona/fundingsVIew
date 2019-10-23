"""
将xml文件的基金描述提取出来
"""
import xml.dom.minidom
import os

filePath = '/Users/haohao/Documents/fundingsView/data/raw/'


def getXMLName():
    print


dom = xml.dom.minidom.parse(filePath)
