from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

import json
import datetime

with open('/Users/barewolf/projects/amazon/config.json') as data_file:    
    data = json.load(data_file)
class EbayApi(object):
    def api(self, keyword):
        try:
            api = Connection(appid=data['ebay_key'], config_file=None)
            response = api.execute('findItemsAdvanced', {'keywords': keyword})
        except ConnectionError as e:
            return(e)

        try:
            x = response.reply.searchResult.item
        except Exception as e:
            return e
        
        # min = x[0].sellingStatus.currentPrice.value
        # title = x[0].title
        #print min,title

        # for i in x:
        #     max = i.sellingStatus.currentPrice.value
            # if float(max) < float(min):
        #         min = max
        #         title = i.title
        # url = x[0].viewItemURL
        # return x[0].sellingStatus.currentPrice.value,url,x[0]
        return x

# print EbayApi().api('182379412103')
# print EbayApi().api('182300477854')
# print EbayApi().api('192047840099')[0].galleryPlusPictureURL

# print EbayApi().api('182379412103')[0].sellingStatus.currentPrice.value # price
# print EbayApi().api('182379412103')[0].viewItemURL # URL
# print EbayApi().api('182379412103')[0].itemId # ID
# print EbayApi().api('182379412103')[0].title # title
# print EbayApi().api('182379412103')[0].galleryPlusPictureURL # image