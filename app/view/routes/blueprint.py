# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Configures the address paths (URL routes)
"""
from flask import Blueprint
from ...controllers.controller import index, login, register, dashboard, logout, about
from ...controllers.srie.sql_injection.controller import sql_injection
from ...controllers.srie.cryptographic_failures.controller import cryptographic_failures
from ...controllers.srie.command_execution.controller import command_execution
from ...controllers.user_profile.controller import user_profile

blueprint = Blueprint('blueprint', __name__, template_folder='../templates', static_folder='../../assets')

# Home
blueprint.route('/')(index)
blueprint.route('/login', methods=['GET', 'POST'])(login)
blueprint.route('/register', methods=['GET', 'POST'])(register)
blueprint.route('/dashboard', methods=['GET', 'POST'])(dashboard)
blueprint.route('/about', methods=['GET', 'POST'])(about)
blueprint.route('/logout', methods=['GET', 'POST'])(logout)

# User Profile
blueprint.route('/user_profile/user_profile', methods=['GET', 'POST'])(user_profile)

# SRIE
blueprint.route('/srie/sql_injection/sql_injection', methods=['GET', 'POST'])(sql_injection)
blueprint.route('/srie/cryptographic_failures/cryptographic_failures', methods=['GET', 'POST'])(cryptographic_failures)
blueprint.route('/srie/command_execution/command_execution', methods=['GET', 'POST'])(command_execution)