# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Business logic for the main application
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

from .sql import db, UserDB, Product
import hashlib

class PyFlaSQL():
    """Create the application PyFlaSQL"""
    def __init__(self):
        self.myapp = self.create_app("config")  # Creating the app

        with self.myapp.app_context():
            db.create_all()
            bcrypt = Bcrypt(self.myapp)

            user = UserDB.query.filter_by(username="admin").first()
            if user is None:
                passwrd= "admin123"
                hashed_password = hashlib.md5(passwrd.encode()).hexdigest()
                new_user = UserDB(username="admin", password=hashed_password, role=666)
                db.session.add(new_user)
                db.session.commit()

            # Ajout des produits s'ils n'existent pas
            if not Product.query.filter_by(name='Chaise').first():
                product1 = Product(name='Chaise', color='Rouge', quantity=10)
                db.session.add(product1)

            if not Product.query.filter_by(name='Table').first():
                product2 = Product(name='Table', color='Bleu', quantity=5)
                db.session.add(product2)

            if not Product.query.filter_by(name='Bureau').first():
                product3 = Product(name='Bureau', color='Marron', quantity=7)
                db.session.add(product3)

            if not Product.query.filter_by(name='Lit').first():
                product4 = Product(name='Lit', color='Beige', quantity=2)
                db.session.add(product4)

            # Validez les changements
            db.session.commit()

        # debug - print the URL map of blueprint (check the console)
        # print(self.myapp.url_map)

        self.login_manager = LoginManager()
        self.login_manager.init_app(self.myapp)
        self.login_manager.login_view = 'blueprint.login'

        @self.login_manager.user_loader
        def load_user(user_id):
            return UserDB.query.get(int(user_id))

    def create_app(self, config_path="config"):
        app = Flask(__name__)
        app.config.from_object(config_path)  # Configuring from Python Files
        app.config['UPLOAD_FOLDER'] = 'uploads'
        app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}
        
        db.init_app(app)
        from ..view.routes.blueprint import blueprint

        app.register_blueprint(blueprint, url_prefix='/')
        
        return app
