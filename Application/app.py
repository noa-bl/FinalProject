from bottle import Bottle, run, request, response
from beaker.middleware import SessionMiddleware
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
import  secrets
from bson import ObjectId

app = Flask(__name__, template_folder='templates')
app.secret_key = secrets.token_hex(16)

# Initialize MongoDB client outside the route to avoid reconnecting on each request
client = MongoClient("mongodb://myUserAdmin:changeme@mongo:27017/?authSource=admin")
db = client.Project
Users = db.Users
Posts = db.Posts


@app.route(rule='/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        session['username'] = request.form.get('username')
        username = session['username']
        password = request.form.get('password')
        try:
            result = Users.find_one({'username':username, 'password':password})
            
            if str(result) != "None":

                postsNum = Posts.count_documents({'username':username})
                user_posts = Posts.find({'username':username}, {'title':1, 'content':1, 'likes':1 ,'_id':1})
                user_posts_list = list(user_posts)
                username = session['username'] 
                return render_template('success.html', postsNum=postsNum, user_posts_list=user_posts_list, username=username)
                
            else:
                return "Failed Login"
            
        except Exception as e:
            return f"can't connect to MongoDB: {e}"

@app.route(rule='/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        session['username'] = request.form.get('username')
        username = session['username']
        password = request.form.get('password')
        try:
            if Users.find_one({'username': username}):
                return "Username already exists"
            else:
                Users.insert_one({'username': username, 'password': password})
                return render_template('success.html', username=username, postsNum=0, user_posts_list=[])
        except Exception as e:
            return f"Error: {e}"
        
@app.route(rule='/newPost', methods=['GET', 'POST'])
def newPost():
    if request.method == 'GET':
        return render_template('newPost.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        username = session.get('username')

        if not title or not content or not username:
            app.logger.error("Title, content, or username not provided")
            return "Title, content, or username not provided", 400

        # Check if the post already exists
        existing_post = Posts.find_one({'username': username, 'title': title})
        if existing_post:
            app.logger.info(f"Post already exists for user {username} with title {title}")
            return "Post already exists", 400

        try:
            # Insert the new post
            Posts.insert_one({'username': username, 'title': title, 'content': content, 'likes': []})
            user_posts = Posts.find({'username': username}, {'title': 1, 'content': 1, 'likes': 1, '_id': 1})
            postsNum = Posts.count_documents({'username': username})
            user_posts_list = list(user_posts)
            username = session['username']
            app.logger.info(f"New post created for user {username} with title {title}")
            return render_template('success.html', username=username, postsNum=postsNum, user_posts_list=user_posts_list)
        except Exception as e:
            app.logger.error(f"Error creating post: {e}")
            return f"Error: {e}", 500
# NEED TO UNDERSTAND ON FRIDAY
@app.route(rule='/likePost', methods=['POST'])
def likePost():
    post_id = request.form.get('post_id')  # Get the post ID from the form data
    username = session.get('username')

    # check if one arg doesn't exist
    if not post_id or not username:
        return "Post ID or username not found", 400

    post = Posts.find_one({'_id': ObjectId(post_id)})

    # if username liked the post, unlike it
    if username in post.get('likes', []):
        result = Posts.update_one(
            {'_id': ObjectId(post_id)},
            {'$pull': {'likes': username}}
        )
        app.logger.info(f"User {username} unliked post {post_id}")
        return "unliked", 200
        
    else:
        result = Posts.update_one(
            {'_id': ObjectId(post_id)},
            {'$addToSet': {'likes': username}}
        )
        app.logger.info(f"User {username} liked post {post_id}")
        return "liked", 200

@app.route('/allPosts')
def allPosts(methods=['GET', 'POST']):
    if request.method == 'GET':
        return render_template('allPosts.html')
    elif request.method == 'POST':
        session['username'] = request.form.get('username')
        username = session['username']
        postsNum = Posts.count_documents()
        posts = Posts.find()
        posts_list = list(posts)
        return render_template('success.html', postsNum=postsNum, posts_list=posts_list, username=username)


@app.route('/getUpdatedPosts')
def getUpdatedPosts():
    username = session.get('username')
    postsNum = Posts.count_documents({'username': username})
    user_posts = Posts.find({'username': username}, {'title': 1, 'content': 1, 'likes': 1, '_id': 1})
    user_posts_list = [
        {
            '_id': str(post['_id']),  # Convert ObjectId to string
            'title': post['title'],
            'content': post['content'],
            'likes': post['likes']
        } for post in user_posts
    ]
    return jsonify({
        'username': username,
        'postsNum': postsNum,
        'user_posts_list': user_posts_list
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)