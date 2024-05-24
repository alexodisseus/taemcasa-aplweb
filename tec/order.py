import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


order = Blueprint('order' , __name__ , url_prefix='/ordem')



@order.route('/', methods = ['GET','POST'])
def index():

    return redirect(url_for('order.list'))
    return "<h3>Legumes Selecionados</h3>"






@order.route('/listar', methods = ['GET','POST'])
def list():
    
    data = model.get_person()
    if data==[]:
        model.add_person()



    data = model.get_all_orders()
    #data = model.get_order()
    print(data)

    

    return render_template('order/list.html' , data=data )





@order.route('/adicionar', methods = ['GET','POST'])
def add():

    """
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
    """
    #trocar por ususario
    usuario = model.get_person()
    usuario_id  = usuario[0].id
    
    #data = False
    data = model.add_order_default(usuario_id)
    
    if data:
        return redirect(url_for('order.list'))

    return render_template('order/add.html')


@order.route('/ver/<id>', methods = ['GET','POST'])
def view(id):
    print(id)
    return render_template('order/view.html')
  






@order.route('/editar', methods = ['GET','POST'])
def edit():

    return "<h3>Legumes Selecionados</h3><p>editar</p>"



@order.route('/apagar', methods = ['GET','POST'])
def delete():

    return "<h3>Legumes Selecionados</h3><p>apagar</p>"




def configure(app):
	app.register_blueprint(order)






