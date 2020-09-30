from . import bp


@bp.route('/hello')
def hello():
    return 'hello'
