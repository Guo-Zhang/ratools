#-*-coding:utf-8-*-

import os
import codecs
import re

def func(arg):
    name,url = arg.split(',')
    url = re.sub('\n','',url)
    return url

def main():
    fname = raw_input('please input the file name: ')
    with codecs.open(fname,'rb') as f:
        urllist = map(func,list(set(f.readlines())))
        
    with codecs.open('urls','wb') as f:
        for i in urllist:
            f.write(i)
            f.write('\n')

main()