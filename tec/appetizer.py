import app
import model

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


appetizer = Blueprint('appetizer' , __name__ , url_prefix='/entrada')




@appetizer.route('/', methods = ['GET','POST'])
def index():


    return "<h3>Legumes Selecionados</h3>"





def configure(app):
	app.register_blueprint(appetizer)






