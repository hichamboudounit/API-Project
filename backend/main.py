from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from fastapi import HTTPException

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@app.get("/suppliers")
def get_suppliers(db: Session = Depends(get_db)):
    return db.query(models.Supplier).all()

@app.get("/inventory")
def get_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()

@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@app.get("/order_items")
def get_order_items(db: Session = Depends(get_db)):
    return db.query(models.OrderItem).all()

@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product