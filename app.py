from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/wifi-data', methods=['GET'])
def get_wifi_data():
    wifi_info = {}
    stats = psutil.net_if_stats()
    for interface, data in stats.items():
        wifi_info[interface] = {
            "is_up": data.isup,
            "speed": data.speed,
            "duplex": data.duplex,
            "mtu": data.mtu
        }
    return jsonify(wifi_info)

# Only include this line for local development
if __name__ == '__main__':
    app.run()  # Remove host and port to make it Vercel-compatible
