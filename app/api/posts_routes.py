from flask import Blueprint, request, session, jsonify
from flask_login import login_required, current_user
from app.models import Post, Photo, User, Comment, Like
from wtforms.validators import DataRequired
from app.forms.post_form import PostForm
from app.forms.comment_form import CommentForm
from datetime import datetime
from app.models import db
import boto3
import botocore
from app.config import Config
from app.aws_s3 import upload_file_to_s3


posts_routes = Blueprint('posts', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

# READ ONE POST


@posts_routes.route("/<int:id>")
@login_required
def get_one_post(id):
    post = Post.query.get(id)
    if post:
        return post.to_dict()
    else:
        return "Post not found", 404

# READ ALL POSTS


@posts_routes.route('/')
@login_required
def posts():
    userId = current_user.id
    user = User.query.get(userId).to_dict()
    results = Post.query.filter(Post.user_id.in_(
        user["following"])).order_by(Post.createdAt.desc()).all()

    results_dict = {post.id: post.to_dict() for post in results}
    print("$$$$$$$$$", results_dict)
    return results_dict


@posts_routes.route('/', methods=["POST"])
@login_required
def create_post():
    print("3333333333333333", "trying to create post")
    form = PostForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    file = request.files["file"]
    file_url = upload_file_to_s3(file, Config.S3_BUCKET)
    post = Post(
        user_id=form.data['user_id'],
        description=form.data['description'],
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )
    db.session.add(post)
    db.session.commit()
    photo = Photo(
        url=file_url,
        user_id=form.data['user_id'],
        post_id=post.id,
        createdAt=datetime.now(),
        updatedAt=datetime.now())
    db.session.add(photo)
    db.session.commit()
    return post.to_dict()


# UPDATE ONE POST
@posts_routes.route("/<int:id>", methods=["PUT"])
def update_post(id):
    post = Post.query.get(id)
    req = request.get_json()
    if post:
        post.description = req
        db.session.commit()
        return post.to_dict()
    else:
        return "Post not found", 404

# DELETE ONE POST


@posts_routes.route("/<int:id>", methods=["DELETE"])
def delete_post(id):
    print('id', id)
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return "Ok", 200
    else:
        return "Post not found", 404


# READ ALL COMMENTS ON ONE POST
@posts_routes.route('/<int:id>/comments')
@login_required
def get_comments(id):
    post = Post.query.get(id)
    if post:
        comments = Comment.query.filter(
            Comment.post_id == id).all()
        comments_dict = {comment.id: comment.to_dict() for comment in comments}

        return comments_dict

# CREATE NEW COMMENT ON ONE POST


@posts_routes.route('/<int:id>/comments', methods=["POST"])
@login_required
def create_comment(id):
    req = request.get_json()
    if req:
        comment = Comment(
            user_id=req['id'],
            content=req['comment'],
            post_id=id,
            createdAt=datetime.now(),
            updatedAt=datetime.now()
        )

        db.session.add(comment)
        db.session.commit()

        return comment.to_dict()

# UPDATE ONE COMMENT


@posts_routes.route("/<int:id>/comments/<int:comment_id>", methods=["PUT"])
@login_required
def update_comment(id, comment_id):
    req = request.get_json()

    comment = Comment.query.get(comment_id)
    if comment:
        comment.content = req['content']
        db.session.commit()
        return comment.to_dict()
    else:
        return "Comment not found", 404

# DELETE ONE COMMENT ON ONE POST


@posts_routes.route("/<int:id>/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(id, comment_id):

    comment = Comment.query.get(comment_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return 'Ok', 200
    else:
        return "Post not found", 404


# CREATE A LIKE
@posts_routes.route("/<int:pid>/likes/<int:uid>", methods=["POST"])
def add_like(uid, pid):
    # req = request.get_json()
    like = Like(
        like=True,
        user_id=uid,
        post_id=pid,
    )
    db.session.add(like)
    db.session.commit()
    return like.to_dict()

@posts_routes.route("/<int:pid>/likes/<int:uid>", methods=["Delete"])
def delete_like(uid, pid):
    like = Like.query.filter(Like.user_id == uid, Like.post_id == pid).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        return like.to_dict()
    else:
        return "Like does not exist", 404
