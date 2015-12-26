# -*- coding: utf-8 -*-
'''
Created on 2015年12月22日

@author: "Kael.Chi"
'''

class YXHand():
    '''
    classdocs
    '''
    from bs4 import BeautifulSoup

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def HandleBoardInfo(self, content_list):
        import re
        self.BO_DEALER = re.findall(u"发牌:(.)", content_list[0])[0]
        self.BO_VULNERABLE = re.findall(u"局况:(..)", content_list[0])[0]
        #print self.BO_DEALER, self.BO_VULNERABLE
        print content_list[1]