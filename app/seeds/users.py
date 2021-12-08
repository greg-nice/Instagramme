from app.models import db, User



# Adds a demo user, you can add other users here if you want
def seed_users():
    natgeo = User(
        username='Nat Geo', email='natgeo@mail.com', password='password')
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    nasa = User(
        username='NASA', email='nasa@mail.com', password='password')

    db.session.add(demo)
    db.session.add(natgeo)
    db.session.add(nasa)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
