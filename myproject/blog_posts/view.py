from flask import render_template,url_for,redirect,request,Blueprint,flash
from flask_login import login_required,current_user
from myproject.blog_posts.forms import BlogPostForm
from myproject.models import BlogPosts
from myproject import db


blog_posts = Blueprint('blog_posts', __name__)

#### CREATE #########

@blog_posts.route('/create',methods=['GET','POST'])
@login_required
def create():
	form = BlogPostForm()

	if form.validate_on_submit():

		blog_post = BlogPosts(title=form.title.data,
							  text =form.text.data,
							  user_id=current_user.id)

		db.session.add(blog_post)
		db.session.commit()
		return redirect(url_for('core.index'))

	return render_template('create.html',form=form)


############ READ #############

@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):

	blog_post = BlogPosts.query.get_or_404(blog_post_id)

	return render_template('blog_post.html',title=blog_post.title,date=blog_post.date,post=blog_post)


####### UPDATE #############


@blog_posts.route('/<int:blog_post_id>/update',methods=['GET','POST'])
@login_required
def update(blog_post_id):
	blog_post = BlogPosts.query.get_or_404(blog_post_id)

	if current_user != blog_post.author:
		abort(403)

	form = BlogPostForm()

	if form.validate_on_submit():

	    blog_post.title = form.title.data
	    blog_post.text = form.text.data
	    db.session.commit()
	    flash('Post updated successfully!')
	    return redirect(url_for('blog_posts.blog_post',blog_post_id=blog_post.id))


	elif request.method == 'GET': 

		form.title.data = blog_post.title
		form.text.data = blog_post.text

	return render_template('create.html',title='Updating',form=form)



######## DELETE #############

@blog_posts.route('/<int:blog_post_id>/delete')
@login_required
def delete(blog_post_id):

	blog_post = BlogPosts.query.get_or_404(blog_post_id)
	if current_user != blog_post.author:
		abort(403)

	db.session.delete(blog_post)
	db.session.commit()
	flash('Blog post deleted!')

	return redirect(url_for('core.index'))








