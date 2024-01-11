from flask_restful import Resource, reqparse
from models.usuario import UserModel

class User(Resource):
        
    def get(self, user_id):
        user = UserModel.find_hotel(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404 # not found
    
    
    def delete(self, hotel_id):
        user = UserModel.find_user(hotel_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'An error ocurred trying to delete the user.'}, 500
            return {'message': 'User deleted.'}, 200
        return {'message': 'User not found.'}, 404
    
class UserRegister(Resource):
    
    def post(self):
        