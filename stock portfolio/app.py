import yfinance as yf
from flask import request, render_template, jsonify, Flask

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    ticker = request.get_json()['ticker']
    data = yf.Ticker(ticker).history(period='1y')
    return jsonify({'currentPrice': data.iloc[-1].close, 'openPrice': data.iloc[-1].open})

if __name__ == '__main__':  # Corrected the equality check
    app.run(debug=True)
