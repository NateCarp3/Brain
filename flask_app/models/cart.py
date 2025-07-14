from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import brain
from flask_app.models import user
from flask_app.models.brain import Brain
from flask_app.models.user import User

class Cart:
    def __init__(self, data):
        self.user_id = data["user_id"]
        self.brain_model_id = data["brain_model_id"]
        self.quantity = data["quantity"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def add_to_cart(cls, data):
        query = "INSERT INTO cart (user_id, brain_model_id, quantity) VALUES (%(user_id)s, %(brain_model_id)s, %(quantity)s);"
        results = connectToMySQL("Brain_Schema").query_db(query, data)
        return results

    @classmethod
    def get_cart_info(cls, data):
        query = "SELECT * FROM user left join cart on user.id = cart.user_id left join brain_model on brain_model.id = cart.brain_model_id where user.id = %(user_id)s;"
        results = connectToMySQL("Brain_Schema").query_db(query, data)
        print(results)
        user = User(results[0])
        print(user)
        for row in results:
            if row['brain_model.id'] == None:
                return user
            brain_data = {
                'id': row['brain_model.id'],
                'material': row['material'],
                'price': row['price'],
                'color': row['color'],
                'description': row['description'],
                'created_at': row['brain_model.created_at'],
                'updated_at': row['brain_model.updated_at']
            }
            brain = Brain(brain_data)
            user.brains.append(brain)
        return user

    @classmethod
    def delete_brain(cls, data):
        query = "DELETE FROM cart WHERE brain_model_id = %(brain_model_id)s and user_id = %(user_id)s;"
        results = connectToMySQL('Brain_Schema').query_db(query, data)
        return results