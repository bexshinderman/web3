from pymongo import MongoClient
client = MongoClient()

db = client.pymongo_test

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

scotts_post = posts.find_one({'author': 'Scott'})
print(scotts_post)
