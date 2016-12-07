#!/usr/bin/env python
# coding: utf-8
def mysterious(ust):                  #定义一个将十六进制代码转换为所代表的字符
       s=""                               #定义一个空字符串
       for i in range(len(ust)/4):        #因为Unicode是4个字符表示一个汉字，每四个一组
           us=ust[i*4:i*4+4]              #取的是四位连续的数字，将列表元素赋给字符串
           s=s+unichr(int(us,16))         #将字符串按照十六进制转换为整形数字，
           print s                        #打印汉字
                                          #再将整形数字转换为unicode
       return s                           #返回类似u'\u5269'的字符串
