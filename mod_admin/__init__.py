from flask import Blueprint


admin = Blueprint('admin',__name__,url_prefix='/admin01/')

@admin.route('/')
def admin_index() :
    return 'Admin comes to scene.'