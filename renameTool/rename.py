#-*-coding:utf-8-*-

import os
import codecs
import re
import random
import string


def func(arg):
    value,key = arg.split(',')
    value = value.replace('*','')
    key = re.sub('\n','',key)
    key = key.split('/')[-1]
    return (key,value)

    
def pdfmapping(fname):
    with codecs.open(fname,'rb',encoding='utf-8') as f:
        pdflist = list(set(f.readlines()))
        pdfdir = dict(list(set(map(func,pdflist))))
        return pdfdir


def randomname(pdfdir,path,fname):
    try:
        s = random.choice(string.lowercase)
        os.rename(os.path.join(path,fname),os.path.join(path,re.sub('.pdf','(%s)'%s+'.pdf',pdfdir[fname])))
    except WindowsError:
        return randomname(fname)


def main():
    path = raw_input('please input your PDF dictionary: ')
    name = raw_input('please input your file name: ')
    pdfdir = pdfmapping(name)
    for fname in os.listdir(path):
        fname = fname.decode('gb18030')
        fname = fname.replace('.pdf','.PDF')
        if fname in pdfdir.keys():
            try:
                os.rename(os.path.join(path,fname),os.path.join(path,pdfdir[fname]))
            except WindowsError:
                s = random.choice(string.lowercase)
                try:
                    os.rename(os.path.join(path,fname),os.path.join(path,re.sub('.pdf','(%s)'%s+'.pdf',pdfdir[fname])))
                except WindowsError:
                    randomname(pdfdir,path,fname)
        
main()
         