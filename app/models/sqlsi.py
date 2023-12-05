# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Communicates with the SQLite database
"""
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialisez l'extension SQLAlchemy
dbsi = SQLAlchemy()

# Définissez vos modèles de table
class User(dbsi.Model):
    __tablename__ = 'users'
    id = dbsi.Column(dbsi.Integer, primary_key=True)
    username = dbsi.Column(dbsi.String(80), unique=True, nullable=False)
    password = dbsi.Column(dbsi.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

class Product(dbsi.Model):
    __tablename__ = 'products'
    id = dbsi.Column(dbsi.Integer, primary_key=True)
    name = dbsi.Column(dbsi.String(120), nullable=False)
    color = dbsi.Column(dbsi.String(30))
    quantity = dbsi.Column(dbsi.Integer)

    def __repr__(self):
        return f'<Product {self.name}>'
