import os
from flask import Blueprint, render_template, redirect, url_for, request , send_from_directory, session,  flash
from flask import jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/opt/term21-webui/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


api= Blueprint('api', __name__,
    static_folder = "./static",
    template_folder = "./views")


@api.route('/')
def home():
    return render_template("app/app.html",state_vars=session)



@api.route('/media/<path:path>')
def apisend_media(path):
    return send_from_directory('static', path)    


@api.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

#app.add_url_rule(
#    "/uploads/<name>", endpoint="download_file", build_only=True
#)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route('/upload', methods=['POST'])

def upload():
    
    success=True
    files=[]
    count=0
    for f in request.files.getlist('textures'):

        if f.filename != '':
            count=count+1
            filename = secure_filename(f.filename)
            new_file=os.path.join(UPLOAD_FOLDER, filename)
            web_path=os.path.join("upload", filename)
            files.append({'file':filename,'path':web_path})

            f.save(new_file)
        else:
            success=False
    
    if count==0:
        success=False
    
    return jsonify(
        success=success,
        count=count,
        files=files
    )