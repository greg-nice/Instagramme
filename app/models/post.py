from .db import db




class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', back_populates='posts')
    like = db.relationship('Like', back_populates='posts')
    comment = db.relationship('Comment', back_populates='posts')
    photo = db.relationship('Photo', back_populates='posts')
