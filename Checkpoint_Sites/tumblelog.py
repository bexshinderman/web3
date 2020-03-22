from mongoengine import *
connect('my_db')



class User(Document):
    email = StringField()
    first_name = StringField()
    last_name = StringField()

bex = User(first_name='Bex', last_name='S')

for u in User.objects:
    u['first_name'] = 'Changed'
    u.save()


