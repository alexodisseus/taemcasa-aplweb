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




@product.route('/ver/<id>', methods = ['GET','POST'])
def view(id):
    id_view = id
    print(id_view)

    data = model.get_view_product(id_view)
    print(data)
    #mudar o html colocar no padrão

    return render_template('product/view.html' , data=data )




@product.route('/adicionar', methods = ['GET','POST'])
def add():

    #talves mudar para adicionar fotos dos produtos tambem
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        data = model.add_product(name,description)
        if data:
            return redirect(url_for('product.list'))
        


    return render_template('product/add.html')




@product.route('/editar/<id>', methods = ['GET','POST'])
def edit(id):

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        
        data = model.edit_product(id, name,description)
        if data:
            return redirect(url_for('product.list'))
        
    data = model.edit_product_get(id)

    return render_template('product/edit.html' , data=data)



@product.route('/apagar', methods = ['GET','POST'])
def delete():

    return "<h3>Legumes Selecionados</h3><p>apagar</p>"




def configure(app):
	app.register_blueprint(product)






