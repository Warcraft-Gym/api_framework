from services.base_service import BaseGNLBackendService
from model.user import User

class UserService(BaseGNLBackendService):
    def getUserByDiscord(self, discord_name):
        user = None
        if not discord_name:
            raise Exception(f"Discrod name not defined: {discord_name}")
        users = self.search_users(f"discord=={discord_name}")
        if not users or len(user) == 0:
             return None
        if len(users) > 1:
            raise Exception(f"More than one user found by discord name: {discord_name}")
        user = users[0]
        return user
    

    def search_users(self, search_string):
        if not search_string:
            raise Exception(f"Search String not defined: {search_string}")
        users = self.search("users/search", search_string)
        l = []
        for user in users:     
            l.append(User(user))
        return l
    
    def get_user(self, user_id : int):
        return User(self.get(f"users/{user_id}"))
    
    def update_user(self, user_id, user: User):
        if not user or not user_id:
            raise Exception(f"User or user id not defined: {user}")
        return User(self.put(f"users/{user_id}", user.to_dict()))
    
    def create_user(self, user: User):
        if not user:
            raise Exception(f"User not defined: {user}")
        return User(self.post("users", user.to_dict()))
    
    def delete_user(self, user_id):
        if not user_id:
            raise Exception(f"User id not defined: {user_id}")
        self.delete(f"users/{user_id}")
        return True
    
    def get_all_users(self):
        users = self.get("users")
        l = []
        for user in users:     
            l.append(User(user))
        return l