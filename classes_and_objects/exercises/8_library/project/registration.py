from project.library import Library
from project.user import User


class Registration:
    def __init__(self):
        pass


    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        else:
            library.user_records.remove(user)

    def change_username(self, user_id:int, new_username:str, library: "Library"):
        current_user = next((u for u in library.user_records if u.user_id == user_id), None)
        if current_user:
            if current_user.username != new_username:
                current_user.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            else:
                return "Please check again the provided username - it should be different than the username used so far!"
        elif not current_user:
            return f"There is no user with id = {user_id}!"