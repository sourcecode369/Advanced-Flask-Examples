from __future__ import absolute_import, division, print_function, unicode_literals
import os
from basic import db, Puppy

# Create
print("Create")
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

# Read
print("Read")
all_puppies = Puppy.query.all()
print(all_puppies)

#Select by Id
print("Select by id")
puppy1 = Puppy.query.get(1)
print(puppy1.name)
print(puppy1.age)

# Filters
print("Filter")
puppy_frankie = Puppy.query.filter_by(name="Rufus")
print(puppy_frankie.all())

#Update
print("Update")
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()
print(Puppy.query.all())

#Delete
print("Delete")
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()
print(Puppy.query.all())

#all puppies
print("All Puppies")
all_puppies = Puppy.query.all()
db.session.commit()
for i in range(len(all_puppies)):
    x = all_puppies.get(i)
    print(x.id, x.name, x.age)
print(all_puppies)