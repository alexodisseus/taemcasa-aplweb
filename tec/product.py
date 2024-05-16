import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


product = Blueprint('product' , __name__ , url_prefix='/produto')








@product.route('/', methods = ['GET','POST'])
def index():

    return "<h3>Legumes Selecionados</h3>"



def get_image_url(item_name):
    query = item_name + " imagem"
    for url in search(query, num=1, stop=1):
        return url







@product.route('/listar', methods = ['GET','POST'])
def list():
    
    data = model.get_person()
    if data==[]:
        model.add_person()

    data = model.get_list_filter_product()
    

    return render_template('product/list.html' , data=data )





@product.route('/adicionar', methods = ['GET','POST'])
def add():

    
    if request.method == 'POST':
        name = request.form['name']
        tag = request.form['tag']
        cost = request.form['cost']
        measure = request.form['measure']
        amount = request.form['amount']

        data = model.add_product(name, tag, cost, measure, amount)
        if data:
            return redirect(url_for('product.list'))
            pass


    return render_template('product/add.html')




@product.route('/editar', methods = ['GET','POST'])
def edit():

    return "<h3>Legumes Selecionados</h3><p>editar</p>"



@product.route('/apagar', methods = ['GET','POST'])
def delete():

    return "<h3>Legumes Selecionados</h3><p>apagar</p>"




def configure(app):
	app.register_blueprint(product)






