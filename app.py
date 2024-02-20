from flask import Flask, jsonify
import os

app = Flask(__name__)

# Charger les variables d'environnement
message = os.getenv("MESSAGE", "Default Message of the Day")
app_port = int(os.getenv("APP_PORT", 5000))

# Endpoint pour obtenir le message du jour (MOTD)
@app.route('/motd', methods=['GET'])
def get_motd():
    return jsonify({"message": message})

if __name__ == '__main__':
    print(f'starting app on port {app_port}')
    app.run(host="0.0.0.0", debug=True, port=app_port)
