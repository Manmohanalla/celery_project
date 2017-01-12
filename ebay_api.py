'''
Ebay Api
'''
import configparser

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

CONFIG = configparser.ConfigParser()
CONFIG._interpolation = configparser.ExtendedInterpolation()
CONFIG.read('config.ini')
KEY = CONFIG.get('ebay_keys', 'key')

class EbayApi(object):
    '''
    Ebay API Class
    '''
    def __init__(self):
        self.key1 = KEY

    def api(self, keyword):
        '''
        ebay api
        '''
        try:
            api = Connection(appid=self.key1, config_file=None)
            response = api.execute('findItemsAdvanced', {'keywords': keyword})
        except ConnectionError as connection_error:
            return connection_error
        try:
            resp = response.reply.searchResult.item
        except Exception as no_result:
            return no_result
        return resp
        