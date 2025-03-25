
# import time
# time.clock = time.time
# import collections.abc
# # from chatterbot.trainers import ChatterBotCorpusTrainer
# # from chatterbot import ChatBot
# from flask import Flask, render_template, request
# from flask_socketio import SocketIO, send
# import pymysql
# from sqlalchemy.engine.url import URL
# from sqlalchemy import create_engine
# import os
# from flask import Flask, render_template, request, redirect
# import stripe







# collections.Hashable = collections.abc.Hashable

# app = Flask(__name__, static_folder='static', template_folder='templates')

# app.config['SECRET'] = "secret!123"
# socketio = SocketIO(app, cors_allowed_origins="*")

# # Set your Stripe secret key here
# stripe.api_key = "sk_test_51Of7HkSFn1z8nH5wval4ZJg0uTMYbSJqMxsPFCYylGaaRERchwGtNTbjUyuJDPGJKbvvS8eG8bARffxaQu82ogKT00s5JpkokC"

# YOUR_DOMAIN = "http://127.0.0.1:8040"

# # chat_bot_instance = ChatBot('ChatBot')
# # trainer = ChatterBotCorpusTrainer(chat_bot_instance)
# # trainer.train("chatterbot.corpus.english")


# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(chat_bot_instance.get_response(userText))


# # def create_table():
# #     conn = pymysql.connect(user='root', password='9907', host='localhost')
# #     c = conn.cursor()
# #     c.execute("CREATE DATABASE IF NOT EXISTS E_CHIKITSALAYA")
# #     c.execute("USE E_CHIKITSALAYA")
# #     c.execute('''
# #         CREATE TABLE IF NOT EXISTS appointments (
# #             id INT AUTO_INCREMENT PRIMARY KEY,
# #             patient_name VARCHAR(255) NOT NULL,
# #             email VARCHAR(255) NOT NULL,
# #             phone VARCHAR(15) NOT NULL,
# #             doctor VARCHAR(50) NOT NULL,
# #             appointment_date DATE NOT NULL,
# #             time TIME NOT NULL,
# #             additional_info TEXT
# #         )
# #     ''')
# #     c.execute('''
# #         CREATE TABLE IF NOT EXISTS newsletter_subscribers (
# #             id INT AUTO_INCREMENT PRIMARY KEY,
# #             email VARCHAR(255) NOT NULL
# #         )
# #     ''')
# #     conn.commit()
# #     conn.close()


# @app.route('/create-checkout-session', methods=['POST'])
# def create_checkout_session():
#     try:
#         checkout_session = stripe.checkout.Session.create(
#             line_items=[
#                 {
#                     'price': 'price_1Of7NWSFn1z8nH5wgHiT228T',
#                     'quantity': 1
#                 }
#             ],
#             mode="subscription",
#             success_url=YOUR_DOMAIN + "/success.html",
#             cancel_url=YOUR_DOMAIN + "/cancel.html",
#             payment_method_types=["card"],
#             billing_address_collection='required',
#             shipping_address_collection={
#                 'allowed_countries': ['US', 'CA'],
#             },
#         )
#     except Exception as e:
#         return str(e)

#     return redirect(checkout_session.url, code=303)


# @socketio.on('message')
# def handle_message(message):
#     print("Received message: " + message)
#     if message != "User connected!":
#         send(message, broadcast=True)


# @app.route('/newsletter', methods=['POST'])
# def newsletter():
#     if request.method == 'POST':
#         email = request.form['email_newsletter']

#         # Insert the email into the database
#         conn, c = sql_connector()
#         c.execute(
#             'INSERT INTO newsletter_subscribers (email) VALUES (%s)', (email,))
#         conn.commit()
#         conn.close()
#         c.close()

#     return redirect('/')


# def sql_connector():
#     conn = pymysql.connect(user='root', password='9907',
#                            db='E_CHIKITSALAYA', host='localhost')
#     c = conn.cursor()
#     return conn, c


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     success_message = None

#     if request.method == 'POST':
#         # Retrieve form data
#         patient_name = request.form['patientName']
#         email = request.form['email']
#         phone = request.form['phone']
#         doctor = request.form['doctor']
#         appointment_date = request.form['appointmentDate']
#         time = request.form['time']
#         additional_info = request.form['message']

#         # Store data in the database
#         conn, c = sql_connector()
#         c.execute(
#             "INSERT INTO appointments (patient_name, email, phone, doctor, appointment_date, time, additional_info) VALUES (%s, %s, %s, %s, %s, %s, %s)",
#             (patient_name, email, phone, doctor,
#              appointment_date, time, additional_info)
#         )
#         conn.commit()
#         conn.close()
#         c.close()

#         # Set success_message if the form is successfully submitted
#         success_message = 'Form submitted successfully!'
#         # Redirect to the same route after successful form submission

#     return render_template('index.html', success_message=success_message)


# @app.route('/chatbot_page')
# def chatbot_page():
#     return render_template('med-bot.html')


# @app.route('/doctor_chat')
# def doctor_chat():
#     return render_template('doctor_chat.html')


# @app.route('/dev_team_detail')
# def dev_team_detail():
#     return render_template('dev-team-detail.html')


# @app.route('/success.html')
# def success():
#     return render_template('success.html')


# @socketio.on('message-video')
# def handle_message(data):
#     socketio.emit('message-video', data)
    
# @app.route('/video_call_doc_html')
# def video_call_doc_html():
#     return render_template('video_call_doc_webrtc.html')




# if __name__ == '__main__':
#     # Change the port number to your desired value, e.g., 8080
#     # create_table()
#     # app.run(port=8080, debug=True)
#     #  socketio.run(app, host='localhost', port=8080, debug=True)
#     # socketio.run(app, host='127.0.0.1', port=8040, debug=True)
#     # socketio.run(app, host='0.0.0.0', port=int(os.getenv("PORT", 10000)), debug=False)
    
#     # socketio.run(app, host='0.0.0.0', port=10000, debug=False)

#     PORT = int(os.environ.get("PORT", 10000))  # Use Render's dynamic port
#     socketio.run(app, host="0.0.0.0", port=PORT, debug=False)


import time
import collections.abc
from flask import Flask, render_template, request, redirect
import pymysql
import stripe
import os

collections.Hashable = collections.abc.Hashable

app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['SECRET'] = "secret!123"

# Set your Stripe secret key here
stripe.api_key = "sk_test_51Of7HkSFn1z8nH5wval4ZJg0uTMYbSJqMxsPFCYylGaaRERchwGtNTbjUyuJDPGJKbvvS8eG8bARffxaQu82ogKT00s5JpkokC"

YOUR_DOMAIN = "http://127.0.0.1:8040"

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1Of7NWSFn1z8nH5wgHiT228T',
                    'quantity': 1
                }
            ],
            mode="subscription",
            success_url=YOUR_DOMAIN + "/success.html",
            cancel_url=YOUR_DOMAIN + "/cancel.html",
            payment_method_types=["card"],
            billing_address_collection='required',
            shipping_address_collection={
                'allowed_countries': ['US', 'CA'],
            },
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


def sql_connector():
    conn = pymysql.connect(user='root', password='9907', db='E_CHIKITSALAYA', host='localhost')
    c = conn.cursor()
    return conn, c

@app.route('/', methods=['GET', 'POST'])
def home():
    success_message = None
    if request.method == 'POST':
        # Retrieve form data
        patient_name = request.form['patientName']
        email = request.form['email']
        phone = request.form['phone']
        doctor = request.form['doctor']
        appointment_date = request.form['appointmentDate']
        time = request.form['time']
        additional_info = request.form['message']

        # Store data in the database
        conn, c = sql_connector()
        c.execute(
            "INSERT INTO appointments (patient_name, email, phone, doctor, appointment_date, time, additional_info) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (patient_name, email, phone, doctor, appointment_date, time, additional_info)
        )
        conn.commit()
        conn.close()
        c.close()
        success_message = 'Form submitted successfully!'
    return render_template('index.html', success_message=success_message)

@app.route('/newsletter', methods=['POST'])
def newsletter():
    if request.method == 'POST':
        email = request.form['email_newsletter']
        conn, c = sql_connector()
        c.execute('INSERT INTO newsletter_subscribers (email) VALUES (%s)', (email,))
        conn.commit()
        conn.close()
        c.close()
    return redirect('/')

@app.route('/success.html')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 10000))
    from gunicorn.app.wsgiapp import run
    run()
