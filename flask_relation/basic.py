from models import db, Puppy, Owner, Toy

# create puppy
rufus = Puppy('Rufus')
kit = Puppy('kity')

db.session.add_all([rufus, kit])
db.session.commit()

all_pup = Puppy.query.all()
print(all_pup)

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# create owner
mejomba = Owner('mojtaba', rufus.id)

# create toy
ball = Toy('ball', kit.id)
pangpang = Toy('pank', kit.id)

db.session.add_all([mejomba, ball, pangpang])
db.session.commit()


rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)


all_pup = Puppy.query.all()
print(all_pup)

all_pup = Puppy.query.all()
for i in all_pup:
	i.report_toys()