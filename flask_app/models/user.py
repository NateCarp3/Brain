from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import brain
from flask_app.models.brain import Brain
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.brains = []

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        results = connectToMySQL("Brain_Schema").query_db(query, data)
        return results

    @classmethod
    def get_user_info(cls, data):
        query = 'SELECT * FROM user WHERE user.id = %(user_id)s;'
        results = connectToMySQL("Brain_Schema").query_db(query, data)
        return results

    @classmethod
    def get_user_info_login(cls, data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL("Brain_Schema").query_db(query, data)
        print(results)
        if len(results) == 0:
            flash("Email or Password Incorrect")
            return results
        return cls(results[0])

    @classmethod
    def get_user_with_brains(cls, data):
        query = "SELECT * FROM user left join brain_model on user.id = brain.user_id left join where user.id = %(user_id)s;"
        results = connectToMySQL("Brain_Schema").query_db(query, data)
        user = cls(results[0])
        print(user)
        for row in results:
            brain_data = {
                'id': row['brain_model.id'],
                'material': row['material'],
                'quantity': row['quantity'],
                'created_at': row['brain_model.created_at'],
                'updated_at': row['brain_model.updated_at']
            }
            brain = brain.Brain(brain_data)
            user.brains.append(brain)
        return user

    @classmethod
    def update_user_info(cls, data):
        query = "UPDATE user SET first_name=%(first_name)s,last_name=%(last_name)s, email=%(email)s WHERE id = %(user_id)s;"
        results = connectToMySQL('Brain_Schema').query_db(query, data)
        return results

    @classmethod
    def delete_user_info(cls, data):
        query = "DELETE from user where id = %(user_id)s;"
        results = connectToMySQL('Brain_Schema').query_db(query, data)
        return results



    @staticmethod
    def validate_user(user):
        is_valid =True
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(user['first_name']) < 2:
            flash('First Name must be greater than 2 characters.')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last Name must be greater than 2 characters.')
            is_valid = False
        if len(user['password']) < 8:
            flash('Last Name must at least 8 characters.')
            is_valid = False
        if user['confirm_password'] != user['password']:
            flash('Your passwords do not match.')
            is_valid = False
        print(is_valid)
        return is_valid