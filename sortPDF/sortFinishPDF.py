#--coding=utf-8--


"""
功能：把已经处理的PDF移动到PDF_FINISH文件夹
"""


import os
import re


def main():
    print u'开始整理'
    
    newpath = 'PDF_FINISH'
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    
    num = 0
    
    for txtname in os.listdir('./TXT'):
        pdfname = re.sub('.txt','.pdf',txtname)
        if pdfname in os.listdir('./PDF'):
            oldfname= os.path.join('./PDF',pdfname)
            newfname = os.path.join(newpath,pdfname)
            os.rename(oldfname,newfname)
            num += 1
            
    print u'本次处理总数：%d'%num
    print u'结束整理'
    
    
if __name__ =='__main__':     
    main()
    input('FINISH')
