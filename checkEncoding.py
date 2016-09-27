# --coding:utf-8--

import os
import codecs

path = raw_input('please input your dict:')
os.chdir(path)
print('-'*10)
for i in os.listdir(os.getcwd()):
    i = i.decode('gb18030')
    if ".txt" in i:
        try:
            with codecs.open(i,'rb',encoding = 'utf-8') as f:
                text = f.read(10)
                print text
                print 'Success:%s'%i 
        except Exception,e:
            print 'Error: cannot open file %s'%i
            print e
        print '-'*10
                

raw_input('finish')
 