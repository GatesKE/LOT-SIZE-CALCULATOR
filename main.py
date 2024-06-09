from flask import Flask, request, render_template

app = Flask(__name__,template_folder='template')

@app.route('/')

def index():

    return render_template('index.html', lot_size=None, form_data={})

@app.route('/calculate', methods=['POST'])

def calculate():
    try:
        risk_amount = float(request.form['risk_amount'])
        commission_per_lot = float(request.form['commission_per_lot'])
        sl_size = float(request.form['sl_size'])
        lot_size = risk_amount / ((10 * sl_size) + commission_per_lot)
        lot_size = round(lot_size, 2)
        form_data = {
            'risk_amount': risk_amount,
            'commission_per_lot': commission_per_lot,
            'sl_size': sl_size
        }
        return render_template('index.html', lot_size=lot_size, form_data=form_data)
    except ValueError:
        form_data = {
            'risk_amount': request.form.get('risk_amount', ''),
            'commission_per_lot': request.form.get('commission_per_lot', ''),
            'sl_size': request.form.get('sl_size', '')
        }
        return render_template('index.html', lot_size="Invalid input. Please enter numerical values.", form_data=form_data)


if __name__ == "__main__":

    app.run(debug=True)
