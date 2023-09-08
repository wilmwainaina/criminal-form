from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Create a SQLite database named 'database.db'
engine = create_engine('sqlite:///database.db')

# Create a base class for declarative models
Base = declarative_base()

# Define the Criminal and Officer tables
class Criminal(Base):
    __tablename__ = 'criminals'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_of_arrest = Column(DateTime, default=datetime.now)
    crime_committed = Column(String, nullable=False)
    officer_id = Column(Integer, ForeignKey('officers.id'))

    officer = relationship('Officer', back_populates='criminals')

class Officer(Base):
    __tablename__ = 'officers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    criminals = relationship('Criminal', back_populates='officer')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


