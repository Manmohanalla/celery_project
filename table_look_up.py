import pymysql.cursors

PRODUCT_ID = 'Product_ID'
DATE_TIME = 'Date_Time' 
PRODUCT_PRICE = 'Product_Price'
PRODUCT_TITLE = 'Product_Title'
PRODUCT_URL = 'Product_URL'
PRODUCT_IMAGE = 'Product_Image'

class LookTables(object):

    def open_connection(self):
        '''creating connection'''
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     db='PointPrice',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def look_table_amazon(self):
        '''
        check data in table
        '''
        connection = self.open_connection()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM amazon"
            cursor.execute(sql, ())
            result = cursor.fetchall()
            connection.close()
            return result

    def look_table_ebay(self):
        '''
        check data in table
        '''
        connection = self.open_connection()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM ebay"
            cursor.execute(sql, ())
            result = cursor.fetchall()
            connection.close()
            return result

x = LookTables().look_table_ebay()
print x[1]
# y = LookTables().look_table_amazon()
# print y[2]['Product_Image']