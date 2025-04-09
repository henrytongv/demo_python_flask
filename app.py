import router
from flask import Flask

app = Flask(__name__)

app.route("/form1", methods=["POST"])(router.guardar_json)
app.route("/form2", methods=["POST"])(router.guardar_json)
app.route("/form3", methods=["POST"])(router.guardar_json)
app.route("/form4", methods=["POST"])(router.guardar_json)

@app.route('/')
def index():
    return 'saludos desde el sur'

if __name__ == "__main__":
    app.run(port=7000, debug=True)
