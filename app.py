from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/teste')
def index():
    return 'TCHAKITCHACKI'

@app.route('/teste/1')
def index1():
    return 'bilsonaro'