from amazon.api import AmazonAPI
from amazon.api import AmazonProduct

import json


with open('/Users/barewolf/projects/amazon/config.json') as data_file:    
    data = json.load(data_file)
class Amazonapi(object):
    
    def search_product(self, keyword):
        amazon = AmazonAPI(data['key1'], data['key2'],\
         data['username'])
        try:
            product = amazon.lookup(ItemId = keyword)
        except Exception as e:
            return e
        return product


