import mlab
from post import Post 

#1.connect
mlab.connect()
#2.creat data
#p= Post(title="c4e21",author="quân",content="sắp đến project rồi", likes=15)
#print(p.title)
#print(p.content)
#print(p.author)
#print(p.likes)
#3. write data
#p.save()
def test_load_data():
    #2. load all documents
    all_posts = Post.objects() #lazy loading

    #3. print all documents
    for post in all_posts:
        print(post.title)
        print(post.content)
        print(post.author)
def test_load_one_data(post_id):
    post= Post.objects().with_id(post_id)
    if post is None :
        print("not found")
    else:
        print(post.title)
        print(post.content)
        print(post.author)

def delete_one_data(post_id):
    #1.retrive document 
    post= Post.objects().with_id(post_id)
    #2.delete document
    if post is None :
        print("post not found")
    else:
        def update_one(post_id, new_title):
    #1.retrive post
    post=Post.objects().with_id(post_id)

    #2.update
    #slug
    post.update(set__title= new_title)
update_one("5ba0fae10f5dbf06d84aff3b" , "photograhy")
        post.delete()
