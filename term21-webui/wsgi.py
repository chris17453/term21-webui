from flask import Flask, request, send_from_directory, jsonify, render_template, session, abort
from flask_login import login_user, logout_user, login_required
from flask_login import LoginManager 
from flask_cors import CORS
from flask.json import JSONEncoder

from pprint import pprint

UPLOAD_FOLDER = '/opt/term21-webui/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, record):
            # Implement code to convert Passport object to a dict
            return obj.to_json()
        else:
            JSONEncoder.default(self, obj)

def create_app():
    app = Flask(__name__, 
    static_folder = "./static",
    template_folder = "./static/views")
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

    app.json_encoder = CustomJSONEncoder
    app.config['SECRET_KEY'] = 'thefirstandlastthingithinkofisapasswordforyou'

    # blueprint for static elements of site
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    
        #print(session)
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("error/404.html",state_vars=session),404

    return app

    

if __name__ == '__main__':
    app=create_app()
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8080
    )
