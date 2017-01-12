'''
Product information from amazon api
'''
import configparser

from amazon.api import AmazonAPI

CONFIG = configparser.ConfigParser()
CONFIG._interpolation = configparser.ExtendedInterpolation()
CONFIG.read('config.ini')
KEY1 = CONFIG.get('amazon_keys', 'key1')
KEY2 = CONFIG.get('amazon_keys', 'key2')
USERNAME = CONFIG.get('amazon_keys', 'username')

class Amazonapi(object): 
    '''
    AMAZON API CLASS
    '''
    def __init__(self):
        self.key1 = KEY1
        self.key2 = KEY2
        self.username = USERNAME

    def search_product(self, keyword):
        '''
        search amazon Products by passing item ID
        '''
        print self.username
        amazon = AmazonAPI(self.key1, self.key2,\
         self.username)
        try:
            product = amazon.lookup(ItemId=keyword)
        except Exception as e:
            return e
        return product
