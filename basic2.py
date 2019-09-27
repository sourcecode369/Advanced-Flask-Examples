from __future__ import absolute_import, print_function, division, unicode_literals
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Puppy, Owner, Toy

# Creating 2 puppies
rufus = Puppy("Rufus")
fido = Puppy("fido")

# Saving
db.session.add_all([rufus, fido])
db.session.commit()

# Printing all the objects
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name="Rufus").first()

print(rufus)

#Assign owner
jose = Owner('Jose',rufus.id)

#Assign Toys
toy1 = Toy("Chew Toy", rufus.id)
toy2 = Toy("Ball", rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

#Grab rufus after those additions
rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)

print(rufus.report_toys())