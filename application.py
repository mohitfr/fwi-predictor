"""Flask routes. Business logic lives in predictor.py and validators.py."""

import os
from flask import Flask, render_template, request, redirect, url_for, session

from config import fields, features, max_fwi_scale
from predictor import FWIPredictor
from validators import validate

application = Flask(__name__)
app = application
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

predictor = FWIPredictor()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/assess', methods=['GET'])
def assess_form():
    return render_template('assess.html', fields=fields, order=features)


@app.route('/assess', methods=['POST'])
def assess_submit():
    values, errors = validate(request.form)

    if errors:
        return render_template(
            'assess.html', fields=fields, order=features,
            errors=errors, submitted=request.form
        )

    fwi = predictor.predict(values)
    risk = predictor.risk_for(fwi)

    session['fwi'] = fwi
    session['risk'] = risk
    session['inputs'] = values

    return redirect(url_for('result'))


@app.route('/result')
def result():
    fwi = session.get('fwi')
    risk = session.get('risk')
    inputs = session.get('inputs')

    if fwi is None:
        return redirect(url_for('assess_form'))

    return render_template(
        'result.html', fwi=fwi, risk=risk, inputs=inputs,
        fields=fields, max_scale=max_fwi_scale
    )


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)