from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    yield db
    db.close()

@app.get("/locations")
def get_locations():
    return ["cpl", "bngr", "ambpt"]

@app.post("/order")
def create_order(name: str, location: str, db: Session = Depends(get_db)):
    order = models.Order(customer_name=name, location=location, status="PLACED")
    db.add(order)
    db.commit()
    return {"message": "Order placed"}

@app.get("/orders/{location}")
def get_orders(location: str, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.location == location).all()
