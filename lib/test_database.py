# test_database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Criminal, Officer

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Add data to the database
officer1 = Officer(name='Officer Smith')
criminal1 = Criminal(name='John Doe', date_of_arrest=datetime.now(), crime_committed='Robbery', officer=officer1)

session.add(officer1)
session.add(criminal1)
session.commit()

# Query the database
print("Criminals:")
criminals = session.query(Criminal).all()
for criminal in criminals:
    print(f"Name: {criminal.name}, Date of Arrest: {criminal.date_of_arrest}, Crime: {criminal.crime_committed}, Officer: {criminal.officer.name}")
