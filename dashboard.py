from flask import Blueprint, render_template, request, jsonify, redirect, url_for

dashboard = Blueprint(__name__,"dashboard")
@dashboard.route("/")
def home():
    return render_template("index.html")

@dashboard.route("/profile")
def profile():
    return render_template("profile.html")

@dashboard.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

# @dashboard.route("/json")
# def get_json():
#     return jsonify({'name':'tim', 'coolness':10})

@dashboard.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@dashboard.route("/go-to-home")
def go_to_home():
    return redirect(url_for("dashboard.home"))