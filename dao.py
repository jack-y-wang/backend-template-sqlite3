from db import db, User

# creates the user with the corresponding arguments if a User
# with either the email or username doesn't already exists
def create_user(name, email, username):
    if name is None or email is None or username is None:
        return None, "Empty name, username, or email"
    optional_user, err = does_user_exist(email, username)
    if optional_user:
        return None, err

    user = User(name=name, email=email, username=username)
    db.session.add(user)
    db.session.commit()
    return user, ""

# checks if a user with either that email or username already exists in the User table
def does_user_exist(email, username):
    optional_user = User.query.filter(User.email==email).first()
    if optional_user:
        return True, f"User with email {email} already exists."
    
    optional_user = User.query.filter(User.username==username).first()
    if optional_user:
        return True, f"User with username {username} already exists."
    
    return False, None

def get_user_by_id(id):
    optional_user = User.query.get(id)
    if optional_user:
        return optional_user, ""
    return None, "User not found."

# get all users stored in the User table
def get_users():
    return User.query.all()
