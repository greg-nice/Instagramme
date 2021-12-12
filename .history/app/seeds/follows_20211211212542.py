from app.models import db, Follow



# Adds a demo user, you can add other users here if you want
def seed_follows():
    f1 = Follow(
        followed_id=1, follower_id=2)
    f2 = Follow(
        followed_id=1, follower_id=3)
    f3 = Follow(
        followed_id=1, follower_id=4)
    f4 = Follow(
        followed_id=1, follower_id=5)
    f5 = Follow(
        followed_id=1, follower_id=6)
    f6 = Follow(
        followed_id=1, follower_id=7)


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
def undo_follows():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
