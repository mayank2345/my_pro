from flask import Flask, render_template, request, make_response, jsonify, json, abort, session, url_for, redirect
from db_session import app, db
from sql_model import UserDetails

@app.route('/')
def home_page():
    return render_template('/home_page.html')

@app.route('/login_page')
def login_page():
    return render_template('/login_page.html')

@app.route('/register_page', methods = ['POST'])
def register_page():
    user_data = request.get_json()
    user = UserDetails(
            username=user_data['username'],
            email_id=user_data['email_id'],
            name=user_data['name'],
            password=user_data['password']
        )
    db.session.add(user)
    db.session.commit()
    return make_response(jsonify({'data':200}))

@app.route('/register_page', methods = ['GET'])
def get_register_page():
    return render_template('register_page.html')

if __name__ == "__main__":
    app.run(debug = True, port= 8000)