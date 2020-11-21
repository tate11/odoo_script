from datetime import datetime
import xmlrpc.client
import psycopg2
import xlrd
import os
import base64


def list_items():
    connection = psycopg2.connect(host="127.0.0.1",
                                  database="product_tmp",
                                  user="postgres",
                                  password="Netlinks@123"
                                  )

    cursor = connection.cursor()
    loc = (os.path.dirname(__file__)+"/Item Master-1.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    items = []

    for r in range(1, 50):
        item = {}
        item['name'] = str(sheet.cell(r, 1).value)
        item['part_number'] = sheet.cell(r, 2).value
        item['default_code'] = sheet.cell(r, 0).value
        cat_id = sheet.cell(r, 3).value
        cursor.execute(
            "select id from product_groups where name =%s", (cat_id,))
        id = cursor.fetchone()
        id = id[0] if id else None
        if os.path.isfile(os.path.dirname(__file__)+"/Item Master-1/"+sheet.cell(r, 4).value):
            f = open(os.path.dirname(__file__) +
                     "/Item Master-1/"+sheet.cell(r, 4).value, "rb")

            coded = base64.b64encode(f.read()).decode("utf-8")
            item['image_1920'] = coded
        items.append(item)
    return items


def xmlrpc_connection():

    url = "http://localhost:8000"
    db = "product_tmp"
    username = 'admin'
    password = "admin"

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    items = list_items()
    models.execute_kw(db, uid, password, 'product.template', 'create', [items])


start_time = datetime.now()
xmlrpc_connection()
print(datetime.now()-start_time)
