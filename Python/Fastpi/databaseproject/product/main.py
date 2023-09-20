from fastapi import FastAPI,status,Response, HTTPException
from fastapi.params import Depends
import schemas
from database import engine , sessionmaker,SessionLocal
import models
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/products')
def fetch_values(db:Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.delete('/products/{id}')
def delete_by_id(id,db:Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {'product deleted'}

@app.put('/product/{id}')
def update(id,request : schemas.Product,db:Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.id == id)
    if not products.first():
        pass
    products.update(request.dict())
    db.commit()
    return {'product successfully updated'}


@app.get('/products/{id}',response_model=List[schemas.DisplayProduct])
def fetch_values_byid(id,response: Response,db:Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.id == id).first()
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")
        response.status_code = status.HTTP_404_NOT_FOUND
    return products


@app.post('/product',status_code=status.HTTP_201_CREATED)
def add(request : schemas.Product,db:Session = Depends(get_db)):
    new_product = models.Product(name=request.name,description=request.description,price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request

@app.post('/seller')
def create_seller(request:schemas.Seller,db:Session = Depends(get_db)):
    new_seller = models.Seller()
    return request