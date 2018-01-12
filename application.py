from flask import Flask,render_template
from flaskrun import flaskrun
from mocks import Post
app= Flask(__name__)


@app.route('/')
def home():
	return render_template('pages/home.html')

@app.route('/contact')
def contact():
	return render_template('pages/contact.html')

@app.route('/about')
def about():
	return render_template('pages/about.html')


@app.route('/blog')
def post_index():
	posts=Post.all()
	return render_template('post/index.html',toto=posts)

@app.route('/blog/post/<int:id>')
def post_show(id):
	post =Post.find(id)
	return render_template('post/show.html',post=post)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__=='__main__':
	flaskrun(app)

