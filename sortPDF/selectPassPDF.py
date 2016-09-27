#-*-coding:utf-8-*-


import os


def main():
    
    if not os.path.exists('./PDF_PASS'):
        os.mkdir('./PDF_PASS')
        
    for fname in os.listdir('./PDF'):
        fname = fname.decode('gb18030')
        if (u'英文' in fname) or (u'已取消' in fname) or (u'补充' in fname):
            old = os.path.join('./PDF',fname)
            new = os.path.join('./PDF_PASS',fname)
            os.rename(old,new)
            print(fname)


main()