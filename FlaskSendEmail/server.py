from flask import Flask, request
from flask_mail import Mail, Message
import base64
from flask_cors import CORS, cross_origin

app = Flask(__name__)
mail= Mail(app)
CORS(app, support_credentials=True)

app.debug = True

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cata.briscan@gmail.com'
app.config['MAIL_PASSWORD'] = "0754651665Cc"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/contact/", methods=['POST'])
@cross_origin(supports_credentials=True)
def index():
   data = request.get_json(force=True)
   print(data)
   msg = Message('Contact Us Online', sender = data['email'], recipients = ['cata.briscan@gmail.com'])
   msg.body = data['message']
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run()
