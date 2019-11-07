#!/usr/bin/env python3

"""Data model of the project."""

import mongoengine as engine

# ENGINES

engine.connect('examples')

# DEFINES

class User(engine.Document):
    """A user of the system."""
    firstname = engine.StringField(max_length=50)
    lastname = engine.StringField(max_length=50)

# INSERTIONS

carrie = User(firstname="Carrie-Anne", lastname="Moss").save()

keanu = User(firstname="Keanu", lastname="Reeves").save()

# SELECTIONS

for user in User.objects:
    print(user.to_json())
