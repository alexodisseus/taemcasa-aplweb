from typing import Optional, List

from sqlmodel import SQLModel ,or_, Field, create_engine, Session, select, Relationship
from sqlalchemy.sql.expression import delete as sql_delete
from sqlalchemy import func


db = SQLModel()

def configure(app):
    app.db = db



class Appetizer(SQLModel, table=True):
	
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	tag:str
	cost:str
	measure:str  
	amount: str



engine = create_engine('sqlite:///db.db')

SQLModel.metadata.create_all(engine)


def list_all(db: Session, question_id: int):
    return db.get(Question, question_id)



