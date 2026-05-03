from flask import Flask, jsonify, send_from_directory
from core.agent_manager import AgentManager

app = Flask(__name__, static_folder='web')
manager = AgentManager()

@app.route('/api/run/<task>')
def run(task):
    return jsonify(manager.dispatch(task))

@app.route('/')
def index():
    return send_from_directory('web', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
