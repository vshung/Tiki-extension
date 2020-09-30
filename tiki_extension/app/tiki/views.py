from flask import render_template, jsonify
from app.tiki import bp
from app.models import Product

@bp.route('/c/<int:pid>')
def test(pid):
    title = 'Lịch sử giá trang Tiki'
    product = Product.filter_by_id(pid)
    prices = []
    for price in product.prices:
        prices.append({
            'date': price.modified_date,
            'price': price.price
        })
    prices.sort(key=lambda x: x['date'], reverse=False)
    prices = prices[:14]

    result = dict()
    result['product'] = {
        'product_id': product.id,
        'product_name': product.product_name,
        'prices': prices
    }
    return render_template('index.html', title=title, result=result)


@bp.route('/p/<int:pid>')
def product_detail(pid):
    product = Product.filter_by_id(pid)
    prices = []
    for price in product.prices:
        prices.append({
            'date': price.modified_date,
            'price': price.price
        })
    prices.sort(key=lambda x: x['date'], reverse=True)
    prices = prices[:14]

    result = dict()
    result['product'] = {
        'product_id': product.id,
        'product_name': product.product_name,
        'prices': prices
    }
    return jsonify(result), 200
