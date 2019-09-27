from basic import db, Puppy

# Creates all the tables model --> db table
db.create_all()
sam = Puppy("Sammy",3, "german shephard")
frank = Puppy("Frankie",4, "bulldog")

db.session.add_all([sam, frank])

db.session.commit()

print(sam)
print(frank)
