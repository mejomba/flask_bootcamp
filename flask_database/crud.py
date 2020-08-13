from app import db, Puppy

# create
rufus = Puppy('rufus', 5)
db.session.add(rufus)
db.session.commit()

# select all
all_puppy = Puppy.query.all()
print(all_puppy)

# select by id
sam = Puppy.query.get(1)
print(sam)
print(sam.name)

# select by filter
frank = Puppy.query.filter_by(name='frankie') # produce some sql code!
print(frank)
print(frank.all())

# update 
frank = Puppy.query.get(2)
frank.age = 10
db.session.add(frank)
db.session.commit()

# delete
rufus = Puppy.query.get(3)
db.session.delete(rufus)
db.session.commit()

all_puppy = Puppy.query.all()
print(all_puppy)
