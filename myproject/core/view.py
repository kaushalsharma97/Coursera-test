from flask import render_template, redirect, Blueprint,request
from myproject.models import BlogPosts

core = Blueprint('core', __name__)

@core.route('/')
def index():
	page = request.args.get('page',1,type=int)
	blog_posts = BlogPosts.query.order_by(BlogPosts.date.desc()).paginate(page=page,per_page=5)
	return render_template('index.html',blog_posts=blog_posts)

@core.route('/info')
def info():
	return render_template('info.html')