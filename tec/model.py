from typing import Optional, List

from sqlmodel import SQLModel ,or_, Field, create_engine, Session, select, Relationship
from sqlalchemy.sql.expression import delete as sql_delete
from sqlalchemy import func


db = SQLModel()

def configure(app):
    app.db = db



class Product(SQLModel, table=True):

	id: Optional[int] = Field(default=None, primary_key=True)
	name: str
	description: str

class Person(SQLModel, table=True):
	
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str
	email: str
	orders: List['Order']=Relationship()






class Order(SQLModel, table=True):

	id: Optional[int] = Field(default=None, primary_key=True)
	person_id: int = Field(foreign_key="person.id")
	#products: List['Person']=Relationship()


class OrderProduct(SQLModel, table=True):
	
	id: Optional[int] = Field(default=None, primary_key=True)
	order_id: int = Field(foreign_key="order.id")
	product_id: int = Field(foreign_key="product.id")
	quantity: int
	price: float
	sold:str #para cintrolar os preço dos produtos que entram
	movement: str #entrada ou saida



engine = create_engine('sqlite:///db.db')

SQLModel.metadata.create_all(engine)



def get_list_filter_order():
	with Session(engine) as session:
		
		query = select(Order)
		data = session.exec(query).all()

		return data

















#product
def get_list_filter_product():
	with Session(engine) as session:
		
		query = select(Product)
		data = session.exec(query).all()

		return data
def get_view_product(id:int):
	with Session(engine) as session:
		
		product = session.get(Product , id)
		

		return product



def add_product(name: str, description: str):
	with Session(engine) as session:
		product = Product(name=name, description=description)
		session.add(product)
		session.commit()
		session.refresh(product)
		return product
		



def edit_product_get(id:int):
	with Session(engine) as session:
		
		product = session.get(Product , id)
		

		return product


def edit_product(id:int, name: str, description: str):
	with Session(engine) as session:
		product = session.get(Product , id)

		if product:
			product.name = name
			product.description = description
			session.commit()
			session.refresh(product)
			return product
		return None



"""
mudar esse trecho para o controle de Person
 |
 V
"""
def add_person():
    with Session(engine) as session:
        new_person = Person(name="default", email='default@gmail.com')
        session.add(new_person)
        session.commit()

def get_person():
	with Session(engine) as session:		
		query = select(Person)
		data = session.exec(query).all()

		return data
"""
mudar esse trecho para o controle de Person
 A
 |
"""
