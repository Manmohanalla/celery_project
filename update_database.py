import pymysql.cursors

PRODUCT_ID = 'Product_ID'
DATE_TIME = 'Date_Time' 
PRODUCT_PRICE = 'Product_Price'
PRODUCT_TITLE = 'Product_Title'
PRODUCT_URL = 'Product_URL'
PRODUCT_IMAGE = 'Product_Image'

class UpdateDatabase(object):

    def open_connection(self):
        '''creating connection'''
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     db='PointPrice',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection


    def add_to_amazon_table(self, Product_ID, Product_Price, Product_Title, Product_URL, Product_Image):
        '''
        adding to table
        '''
        connection = self.open_connection()
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO amazon (PRODUCT_ID, PRODUCT_PRICE, PRODUCT_TITLE, PRODUCT_URL, PRODUCT_IMAGE, DATE_TIME) VALUES (%s, %s, %s, %s, %s, now())"
            try:
                cursor.execute(sql, (Product_ID, Product_Price, Product_Title, Product_URL, Product_Image))
            except Exception as e:
                connection.close()
                return e
            connection.commit()
            connection.close()
            return True

    def add_to_ebay_table(self, Product_ID, Product_Price, Product_Title, Product_URL, Product_Image):
        '''
        adding to table
        '''
        connection = self.open_connection()
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO ebay (PRODUCT_ID, PRODUCT_PRICE, PRODUCT_TITLE, PRODUCT_URL, PRODUCT_IMAGE, DATE_TIME) VALUES (%s, %s, %s, %s, %s, now())"
            try:
                cursor.execute(sql, (Product_ID, Product_Price, Product_Title, Product_URL, Product_Image))
            except Exception as e:
                connection.close()
                return e
            connection.commit()
            connection.close()
            return True

    def update_amazon_table(self, Product_ID, Product_Price ):
        '''
        updatating table
        '''
        connection = self.open_connection()
        with connection.cursor() as cursor:
            # updatd a record
            sql = "UPDATE amazon SET PRODUCT_PRICE = %s, DATE_TIME = NOW() WHERE PRODUCT_ID = %s"
            try:
                cursor.execute(sql, (Product_Price, Product_ID))
            except Exception as e:
                connection.close()
                return e
            connection.commit()
            connection.close()
            return True

    def update_ebay_table(self, Product_ID, Product_Price ):
        '''
        updatating table
        '''
        connection = self.open_connection()
        with connection.cursor() as cursor:
            # updatd a record
            sql = "UPDATE ebay SET PRODUCT_PRICE = %s, DATE_TIME = NOW() WHERE PRODUCT_ID = %s"
            try:
                cursor.execute(sql, (Product_Price, Product_ID))
            except Exception as e:
                connection.close()
                return e
            connection.commit()
            connection.close()
            return True
