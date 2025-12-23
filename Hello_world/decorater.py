from flask import Flask


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authentication_decorater(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authentication_decorater
def create_blog(user):
    print(f"This blog is created by {user.name}")

new_user = User("Dinesh")
new_user1 = User("Ganesh")
new_user2 = User("Mahesh")
# new_user.is_logged_in = True
new_user2.is_logged_in = False
new_user1.is_logged_in = True
create_blog(new_user)
