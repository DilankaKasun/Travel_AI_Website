
from flask import render_template, redirect, request, url_for,session
from apps.payment import blueprint
from apps.payment.forms import LoginForm
import os
import stripe
from flask import render_template, request
from flask_login import login_required


stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'


@blueprint.route('/payment')
@login_required
def tool():
    login_form = LoginForm(request.form)
    return render_template("payment/payment.html",form=login_form)

@blueprint.route('/create-checkout-session', methods=['POST'])
@login_required
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='/success.html',
            cancel_url='/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


