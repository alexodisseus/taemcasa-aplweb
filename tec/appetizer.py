import app
import model

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


appetizer = Blueprint('appetizer' , __name__ , url_prefix='/entrada')










@appetizer.route('/', methods = ['GET','POST'])
def index():

    return "<h3>Legumes Selecionados</h3>"




@appetizer.route('/listar', methods = ['GET','POST'])
def list():



    if request.method == 'POST':

        data = model.get_list_appetizer()
        print(data)



    return render_template('appetizer/list.html')





@appetizer.route('/adicionar', methods = ['GET','POST'])
def add():

    

    data = add_appetizer()

    return "<h3>Legumes Selecionados</h3><p>adicionar</p>"



@appetizer.route('/editar', methods = ['GET','POST'])
def edit():

    return "<h3>Legumes Selecionados</h3><p>editar</p>"



@appetizer.route('/apagar', methods = ['GET','POST'])
def delete():

    return "<h3>Legumes Selecionados</h3><p>apagar</p>"




def configure(app):
	app.register_blueprint(appetizer)






