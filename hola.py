from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

# CRUD (create, read, update, delete)  REST API simple

# Get Data Routes
@app.route('/products')
def getProducts():
    return jsonify({'products': products})


@app.route('/products/<string:product_id>')
def getProduct(product_id):
    productsFound = [
        product for product in products if product['id'] == product_id]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'mensaje': 'Producto No Encontrado'})
    
# Create Data Routes
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'id': request.json['id'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'mensaje': 'Producto Nuevo','products': products})

# Update Data Route
@app.route('/products/<string:product_id>', methods=['PUT'])
def editProduct(product_id):
    productsFound = [product for product in products if product['id'] == product_id]
    if (len(productsFound) > 0):
        productsFound[0]['id'] = request.json['id']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Producto Actualizado',
            'product': productsFound[0]
        })
    return jsonify({'mensaje': 'Producto No Encontrado'})

# DELETE Data Route
@app.route('/products/<string:product_id>', methods=['DELETE'])
def deleteProduct(product_id):
    productsFound = [product for product in products if product['id'] == product_id]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'mensaje': 'Producto Borrado',
            'products': products
        })

if __name__ == '__main__':
    app.run(debug=True, port=8080)


