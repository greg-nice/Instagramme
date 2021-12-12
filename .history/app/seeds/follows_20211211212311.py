from app.models import db, User



# Adds a demo user, you can add other users here if you want
def seed_users():
    f1 = User(
        followed_id=1, follower_id=1)
    f2 = User(
        followed_id=1, follower_id=1)
    f3 = User(
        followed_id=4, follower_id=1)
    f4 = User(
        followed_id=5, follower_id=1)
    f5 = User(
        followed_id=6, follower_id=1)
    f6 = User(
        followed_id=7, follower_id=1)


    db.session.add(f1)
    db.session.add(f2)
    db.session.add(f3)
    db.session.add(f4)
    db.session.add(f5)
    db.session.add(f6)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
