#import admin
#import painel

import model
import order
import product


from flask import Flask
from flask_bootstrap import Bootstrap4

db = model


app = Flask(__name__)
app.config['TITLE'] = "TaEmCasa - Legumes"
app.secret_key = b'guerra aos senhores'


#admin.configure(app)
order.configure(app)
product.configure(app)
db.configure(app)

Bootstrap4(app)