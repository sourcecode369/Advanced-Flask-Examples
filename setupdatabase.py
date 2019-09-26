from basic import db, Puppy

# Creates all the tables model --> db table
db.create_all()
sam = Puppy("Sammy",3)
frank = Puppy("Frankie",4)

db.session.add_all([sam, frank])

db.session.commit()

print(sam)
print(frank)
