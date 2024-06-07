from flask import Flask, request, render_template

app = Flask(__name__,template_folder='template')

def calculate_lot_size(risk_amount, commission_per_lot, sl_size):

    # Lot size calculation formula
    lot_size = risk_amount / ((10 * sl_size) + commission_per_lot)

    #Rounding the lot size to 2 decimal places
    lot_size = round(lot_size, 2)

    return lot_size

@app.route('/')

def index():

    return render_template('index.html', lot_size=None)

@app.route('/calculate', methods=['POST'])

def calculate():

    risk_amount = float(request.form['risk_amount'])

    commission_per_lot = float(request.form['commission_per_lot'])

    sl_size = float(request.form['sl_size'])
    
    lot_size = calculate_lot_size(risk_amount, commission_per_lot, sl_size)

    
    return render_template('index.html', lot_size=lot_size)


if __name__ == "__main__":

    app.run(debug=True)
