from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Brain:
    def __init__(self, data):
        self.id = data['id']
        self.material = data['material']
        self.price = data['price']
        self.description = data['description']
        self.color = data['color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.brain_buyer = ''

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM brain_model join user on user_id = user.id;"
        results = connectToMySQL("Brain_Schema").query_db(query)
        print(results)
        brains = []
        for brain in results:
            x = cls(brain)
            x.brain_buyer = brain['first_name']
            brains.append(x)
        return brains

    @classmethod
    def add_brain(cls, data):
        query = "INSERT INTO brain_model (material, price, description, color) VALUES %(material)s, %(price)s, %(description)s, %(color)s;"
        results = connectToMySQL("Brain_Schema").query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM brain_model;"
        results = connectToMySQL("Brain_Schema").query_db(query)
        brains = []
        for brain in results:
            x = cls(brain)
            brains.append(x)
        return brains

    @staticmethod
    def validate_brain(brain):
        is_valid =True
        if len(brain['quantity']) < 0:
            flash('Quantity must be greater than 0.')
            is_valid = False
        print(is_valid)
        return is_valid