# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for SQL injection
"""
from flask import render_template, url_for, request
from flask_login import login_required
# from flask_migrate import Migrate
import hashlib
from ....models.sql import db, UserDB
from sqlalchemy.sql import text

@login_required
def sql_injection():
    result = None
    error = None

    if request.method == 'POST':
        try:
            user_input = request.form.get('user_input')
            raw_query = text(f"SELECT DISTINCT * FROM product WHERE name = '{user_input}'")
            connection = db.engine.connect()
            result = connection.execute(raw_query).fetchall()
            connection.close()
        except Exception as e:
            error = str(e)
    
    return render_template(url_for('blueprint.sql_injection')+'.html', content={"injection_result": result, "error": error})

