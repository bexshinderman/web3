from mongoengine.document import Document
from mongoengine.fields import DateTimeField, IntField, StringField, URLField
from mongoengine import *
connect('countries')
class Country(Document):
 
    name = StringField(max_length=80, required=True)
    code = StringField(max_length=10, required=True)
    population = IntField(required=True)

nz = Country(name='New Zealand' code='NZ', population=45000000)

for countries in Country.objects:
    countries.save()
