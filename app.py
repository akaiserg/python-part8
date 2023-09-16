from flask import Flask, render_template, request

app = Flask(__name__)
posts = {
    0: {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}

@app.route('/', methods=['GET'])
def home():
    return 'Hello, world!'

@app.route('/post/create', methods=['POST'])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    post_id = len(posts)
    posts[post_id] = {
        'id': post_id,
        'title': title,
        'content': content
    }
    print('here')
    return f"created with id {post_id}"


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = posts.get(post_id)
    #return  f"post {post['title']}, content: \n\n {post['content']}"
    return  render_template('post.html',post=posts.get(post_id))

if __name__ == '__main__':
    app.run(debug=True)
