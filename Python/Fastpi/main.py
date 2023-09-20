from fastapi import FastAPI, Form
from pydantic import BaseModel, Field, HttpUrl
from typing import List,Set
from uuid import UUID
from datetime import date, time,timedelta,datetime

app = FastAPI()

class Profile(BaseModel):
    name : str
    email : str
    age : int


class Event(BaseModel):
    Event_id:UUID
    startdate:date
    starttime:datetime
    repeattime:time
    executeafter:timedelta


class Product(BaseModel):
    name:str
    price:int = Field(title="Price value",gt=0,lt=100)
    discount:int
    discount_price:float
    tags: Set[str] = []

    class Config:
        schema_extra = {
        'example': {
            'name':'ggg',
            'price':10,
            'discount':4,
            'discount_price':0,
            'tags':[1,2,3,4]
        }
        }


@app.post('/addproduct/{product_id}')
def addproduct(product:Product,product_id:int,category:str):
    product.discount_price = product.price - (int(product.price)/100)
    return {"product id": product_id,"category":category}

@app.post('/addevent')
def addevent(event : Event):
    return event

@app.post("/purchase")
def purchase (product:Product,profile:Profile):
    return {'product':product,'profile':profile}

@app.post("/login")
def login(username:str = Form(...),password:str=Form(...)):
    return {'username':username}


@app.post("/")
def add_profile(profile:Profile):
    return profile




@app.get('/')
def index():
    return 'hello world'


# id here is the path parameter

@app.get("/property/{id}")
def property(id:int):
    return {f'property {id}'}

@app.get("/products")
def property(id:int = 1,price=0):
    return {f'property {id} and price {price}'}

#using path parameter and query parameter in the same route
@app.get("/products/{iser_id}/commentss")
def get_comments(iser_id:int,comments):
    return {f'The value is {iser_id} and comments is {comments}'}
