
"""
Implements the logic for Command Execution
"""
from flask import render_template, url_for, request
from flask_login import login_required
from ...utils import get_shell_output
# from flask_migrate import Migrate
import hashlib

@login_required
def command_execution():
    result = None
    error = None

    if request.method == 'POST':
        try:
            result = get_shell_output(f"nmap {request.form.get('user_input')}")
        except Exception as e:
            error = str(e)
    
    return render_template(url_for('blueprint.command_execution')+'.html', content={"result": result, "error": error})

