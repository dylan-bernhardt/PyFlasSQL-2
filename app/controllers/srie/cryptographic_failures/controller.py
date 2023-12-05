# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP1 - Reconnaissance Footprint
"""
from flask import render_template, url_for, request
from flask_login import login_required
# from flask_migrate import Migrate
import hashlib
from ....models.sql import db, UserDB

@login_required
def cryptographic_failures():
    post_data = None
    Erreur = None
    if request.method == 'POST':
        if not UserDB.query.filter_by(username=request.form['username'],).first():
            post_data = {
                'username': request.form['username'],
                'password': hashlib.md5(request.form['password'].encode()).hexdigest()
            }
            hashed_password = hashlib.md5(post_data["password"].encode()).hexdigest()
            new_user = UserDB(username=post_data["username"], password=hashed_password, role=666)
            db.session.add(new_user)
            db.session.commit()
        else :
            Erreur = "Nom d'utilisateur déja existant, merci d'en choisir un autre."
    return render_template(url_for('blueprint.cryptographic_failures')+'.html', post_data=post_data, erreur=Erreur)
