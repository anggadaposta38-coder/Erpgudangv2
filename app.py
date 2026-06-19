from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Selamat Datang di SAP SPWH Web ERP</h1><p>Sistem ini sedang berjalan di Flask!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)