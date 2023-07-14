from flask import Flask
from dashboard import dashboard

app = Flask(__name__)
app.register_blueprint(dashboard, url_prefix="/dashboard")

if __name__== '__main__':
    app.run(debug=True,port = 8000)