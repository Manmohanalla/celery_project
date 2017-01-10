from celery import Celery
from celery.schedules import crontab
from amazonapi import Amazonapi
from ebay_api import EbayApi
from update_database import UpdateDatabase
from check_tables import CheckTables

app = Celery('tasks', backend='amqp', broker='amqp://guest:guest@localhost')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    '''
    Scheduling tasks
    '''
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        get_prices_amazon.s(),
    )
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        get_prices_ebay.s(),
    )

app.conf.timezone = 'US/Pacific'

@app.task
def get_prices_amazon():
    '''
    Getting Amazon data
    '''
    product_ids = ('B01LYT95XR, B01E3SNO1G, B01LRLJV28')
    amazon_api = Amazonapi()
    amazon_products = amazon_api.search_product(product_ids)
    for i in amazon_products:
        product_price = i.price_and_currency[0]
        product_title = i.title
        product_url = i.offer_url
        product_id = i.asin
        product_image = i.large_image_url
        check_table = CheckTables()
        check_result = check_table.check_table_amazon(product_id)
        update_database = UpdateDatabase()
        if check_result:
            result = update_database.update_amazon_table(product_id, product_price)
        else:
            result = update_database.add_to_amazon_table(product_id, product_price,\
                        product_title, product_url, product_image)
    return result

@app.task
def get_prices_ebay():
    '''
    Getting ebay data
    '''
    ebay_api = EbayApi()
    product_id = ['182379412103', '182300477854', '192047840099']
    for i in product_id:
        ebay_product = ebay_api.api(i)[0]
        product_price = ebay_product.sellingStatus.currentPrice.value
        product_title = ebay_product.title
        product_url = ebay_product.viewItemURL
        product_id = ebay_product.itemId
        product_image = ebay_product.galleryURL
        check_table = CheckTables()
        check_result = check_table.check_table_ebay(product_id)
        update_database = UpdateDatabase()
        if check_result:
            result = update_database.update_ebay_table(product_id, product_price)
        else:
            result = update_database.add_to_ebay_table(product_id, product_price,\
                        product_title, product_url, product_image)
    return result
