from flask import Flask

from routes import Paciente, Profesional


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


app.register_blueprint(Paciente.main, url_prefix='/api/pacientes')
app.register_blueprint(Profesional.main, url_prefix='/api/profesionales')

app.run(host='0.0.0.0', port=81)