from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({
        'message': 'Pong!'
    })

@app.route('/products')
def getProducts():
    return jsonify({'products': products})

@app.route('/products/<string:product_name>')
def getProduct(product_name): # Parametro con mismo nombre que lo recibi en la route
    products_found = [product for product in products if product['name'] == product_name]
    if len(products_found) > 0:
        return jsonify({'product': products_found[0]})
    
    return jsonify({
        'message': 'Product not found'
    })
    

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = request.json
    products.append(new_product)
    print(request.json)
    return jsonify({
        'message': 'Product added succesfully',
        'products': products
    })

@app.route('/products/<string:product_name>', methods=['PUT'])
def editEntireProduct(product_name):
    products_found = [product for product in products if product['name'] == product_name]

    if len(products_found) > 0:
        products_found[0]['name'] = request.json['name']
        products_found[0]['price'] = request.json['price']
        products_found[0]['quantity'] = request.json['quantity']

        return jsonify({
            'message': 'Product edited entirely and succesfully',
            'product': products_found[0]
        })
    else:
        return jsonify({
            'message': 'Product not found'
        })


@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    products_found = [product for product in products if product['name'] == product_name]

    if len(products_found) > 0:
        products.remove(products_found[0])
        return jsonify({
            'message': 'Product deleted succesfully',
            'products': products
        })
    else:
        jsonify({
            'message': 'Product not found'
        })


if __name__=="__main__":
    app.run(debug=True, port=4000)