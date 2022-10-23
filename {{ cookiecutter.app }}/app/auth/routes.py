import requests

from flask import render_template, redirect, url_for, current_app, request
from flask_babel import _
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from helpers import is_access_token_valid, is_id_token_valid, oauth_config

from app.auth import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    # get request params
    query_params = {'client_id': oauth_config["client_id"],
                    'redirect_uri': oauth_config["redirect_uri"],
                    'scope': "openid email profile",
                    'state': current_app.config["APP_STATE"],
                    'nonce': current_app.config["NONCE"], 
                    'response_type': 'code',
                    'response_mode': 'query'}

    # build request_uri
    request_uri = "{base_url}?{query_params}".format(
        base_url=current_app.config["auth_uri"],
        query_params=requests.compat.urlencode(query_params)
    )

@bp.route("/authorization-code/callback")
def callback():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    code = request.args.get("code")
    if not code:
        return "The code was not returned or is not accessible", 403
    query_params = {'grant_type': 'authorization_code',
                    'code': code,
                    'redirect_uri': request.base_url
                    }
    query_params = requests.compat.urlencode(query_params)
    exchange = requests.post(
        oauth_config["token_uri"],
        headers=headers,
        data=query_params,
        auth=(oauth_config["client_id"], oauth_config["client_secret"]),
    ).json()

    # Get tokens and validate
    if not exchange.get("token_type"):
        return "Unsupported token type. Should be 'Bearer'.", 403
    access_token = exchange["access_token"]
    id_token = exchange["id_token"]

    if not is_access_token_valid(access_token, oauth_config["issuer"]):
        return "Access token is invalid", 403

    if not is_id_token_valid(id_token, oauth_config["issuer"], oauth_config["client_id"], current_app.config["NONCE"]):
        return "ID token is invalid", 403

    # Authorization flow successful, get userinfo and login user
    userinfo_response = requests.get(oauth_config["userinfo_uri"],
                                     headers={'Authorization': f'Bearer {access_token}'}).json()

    unique_id = userinfo_response["sub"]
    user_email = userinfo_response["email"]
    user_name = userinfo_response["given_name"]

    login_user(unique_id)

    return redirect(url_for("/"))


@bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
