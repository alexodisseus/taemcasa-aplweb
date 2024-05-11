import app
import model

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


appetizer = Blueprint('appetizer' , __name__ , url_prefix='/entrada')










@appetizer.route('/', methods = ['GET','POST'])
def index():

    return "<h3>Legumes Selecionados</h3>"




@appetizer.route('/listar', methods = ['GET','POST'])
def list():



    
    data = model.get_list_appetizer()
    print(data)



    return render_template('appetizer/list.html')





@appetizer.route('/adicionar', methods = ['GET','POST'])
def add():

    
    if request.method == 'POST':
        name = request.form['name']
        tag = request.form['tag']
        cost = request.form['cost']
        measure = request.form['measure']
        amount = request.form['amount']

        data = model.add_appetizer(name, tag, cost, measure, amount)
        if data:
            print(data)
            return redirect(url_for('appetizer.list'))
            pass


    return render_template('appetizer/add.html')




@appetizer.route('/editar', methods = ['GET','POST'])
def edit():

    return "<h3>Legumes Selecionados</h3><p>editar</p>"



@appetizer.route('/apagar', methods = ['GET','POST'])
def delete():

    return "<h3>Legumes Selecionados</h3><p>apagar</p>"




def configure(app):
	app.register_blueprint(appetizer)






