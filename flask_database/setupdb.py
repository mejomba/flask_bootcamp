from app import db, Puppy

db.create_all()

sam = Puppy('sammy', 3)
frank = Puppy('frankie', 4)

db.session.add_all([sam, frank])
print(sam.id)
print(frank.id)
db.session.commit()
print(sam.id)
print(frank.id)
