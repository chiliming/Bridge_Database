'''
Created on 2015年12月22日

@author: "Kael.Chi"
'''

class YXHand():
    '''
    classdocs
    '''
    from bs4 import BeautifulSoup

    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    def HandleInputText(self, content):
        soup = BeautifulSoup(content, "html.parser")

        