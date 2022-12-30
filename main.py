from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    cnx = mysql.connector.connect(user='root', password='11megan11',
                                  host='localhost',
                                  database='api')
    csr = cnx.cursor()
    csr.execute("select username from api.user")
    name = csr.fetchone()
    cnx.close()
    gname = name[0]
    return {gname}


@app.get("/item/{item}")
def get_item(item):
    cnx = mysql.connector.connect(user='root', password='11megan11',
                                  host='localhost',
                                  database='WM370BASD')
    csr = cnx.cursor()
    csr.execute('select stbrcd,STSTYD,STHTS from wm370basd.ststyl00 where ststyl=%s', (item,))
    name = csr.fetchall()
    cnx.close()
    for x in name:
        barcode = x[0]
        desc = x[1]
        harm = x[2]

    tbarcode = barcode.strip()
    tdesc = desc.strip()
    tharm = harm.strip()

    return {"barcode": tbarcode, "Description": tdesc, "Harm Code": tharm}





