import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
import json
class EbayApi(object):
    def api(self, keyword):
        try:
            api = Connection(appid='Manmohan-pricecom-PRD-c45f30466-e103f8bb', config_file=None)
            response = api.execute('findItemsAdvanced', {'keywords': keyword})
        except ConnectionError as e:
            return(e)
            print(e.response.dict())

        try:
            x = response.reply.searchResult.item
        except Exception as e:
            return e
        
        min = x[0].sellingStatus.currentPrice.value
        title = x[0].title
        #print min,title
        for i in x:
            max = i.sellingStatus.currentPrice.value
            if float(max) < float(min):
                min = max
                title = i.title
        return min

