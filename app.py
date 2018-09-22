from flask import Flask , render_template  ,request , redirect , url_for
import mlab
from post import Post
app =Flask(__name__)
mlab.connect()


@app.route("/post/<post_id>")
def post(post_id):
    post = Post.objects().with_id(post_id)
    return render_template("post.html", post=post)
@app.route("/delete/<post_id>")
def delete_one_data(post_id):

    #1.retrive document 
    post= Post.objects().with_id(post_id)
    #2.delete document
    if post is None :
        print("post not found")
    else:
        post.delete()    
        return  redirect(url_for("posts"))



@app.route("/update/<post_id>")
def update(post_id, new_title):
    
    post=Post.objects().with_id(post_id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    elif request.method == 'POST':
        form= request.form 
        t=form['title']
        a= form['author']
        c =form['content']
        post.update(set__title= t , set__author= a, set__content=c)


@app.route("/posts")
def posts():
    all_posts = Post.objects()
    return render_template("posts.html", posts=all_posts)
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    elif request.method == "POST":
        #1. get form & extract data
        form = request.form
        t = form["title"]
        a=form["author"]
        c =form["content"]
        
       
        new_post=Post(title=t , author=a, content=c )
        new_post.save()
        return redirect(url_for("posts"))
if __name__ == "__main__":
    app.run(debug=True)