import pymysql.cursors

PRODUCT_ID = 'Product_ID'
DATE_TIME = 'Date_Time' 
PRODUCT_PRICE = 'Product_Price'
PRODUCT_TITLE = 'Product_Title'
PRODUCT_URL = 'Product_URL'
PRODUCT_IMAGE = 'Product_Image'

class CheckTables(object):

    def open_connection(self):
        '''creating connection'''
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     db='PointPrice',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def check_table_amazon(self, product_id):
        '''
        check data in table
        '''
        connection = self.open_connection()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM amazon where Product_ID = %s "
            cursor.execute(sql, ( product_id))
            result = cursor.fetchone()
            connection.close()
            return result
   
    def check_table_ebay(self, product_id):
        '''
        check data in table
        '''
        connection = self.open_connection()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM ebay where Product_ID = %s "
            cursor.execute(sql, (product_id))
            result = cursor.fetchone()
            connection.close()
            return result

