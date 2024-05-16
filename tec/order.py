import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


order = Blueprint('order' , __name__ , url_prefix='/entrada')










@order.route('/', methods = ['GET','POST'])
def index():

    return "<h3>Legumes Selecionados</h3>"



def get_image_url(item_name):
    query = item_name + " imagem"
    for url in search(query, num=1, stop=1):
        return url







@order.route('/listar', methods = ['GET','POST'])
def list():
    
    data = model.get_person()
    if data==[]:
        model.add_person()

    data = model.get_list_filter_order()
    

    return render_template('order/list.html' , data=data )





@order.route('/adicionar', methods = ['GET','POST'])
def add():

    
    if request.method == 'POST':
        name = request.form['name']
        tag = request.form['tag']
        cost = request.form['cost']
        measure = request.form['measure']
        amount = request.form['amount']

        data = model.add_order(name, tag, cost, measure, amount)
        if data:
            return redirect(url_for('order.list'))
            pass


    return render_template('order/add.html')




@order.route('/editar', methods = ['GET','POST'])
def edit():

    return "<h3>Legumes Selecionados</h3><p>editar</p>"



@order.route('/apagar', methods = ['GET','POST'])
def delete():

    return "<h3>Legumes Selecionados</h3><p>apagar</p>"




def configure(app):
	app.register_blueprint(order)





