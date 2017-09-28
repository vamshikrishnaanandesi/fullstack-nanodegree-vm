from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

#The return value of create_engine() is an instance of Engine, and it represents the core interface to the database, adapted through a dialect that handles the details of the database and DBAPI in use.
engine = create_engine('sqlite:///restaurantmenu.db')

#Mapping using declarative_base class
Base.metadata.bind = engine

#The ORMs handle to the database is the Session
DBSession = sessionmaker(bind = engine)
session = DBSession()

#creating an instance using query class
firstResult = session.query(Restaurant).first()

r_name = session.query(Restaurant).all()
for names in r_name:
	print names.name



items = session.query(MenuItem).all()

for item in items:
	print item.name

UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 2).one()

UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()


veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
	if veggieBurger.price != '$2.99':
		veggieBurger.price = '$2.99'
		session.add(veggieBurger)
		session.commit()


for veggieBurger in veggieBurgers:
	print veggieBurger.id
	print veggieBurger.price
	print veggieBurger.restaurant.name
	print "\n"

print(firstResult.name)

#spinach = session.query(MenuItem).filter_by(id = 91).all()

#session.delete(spinach)
#1ession.commit()


#spinach = session.query(MenuItem).filter_by(id = 91).one()
