import flask
import werkzeug
import os

app = flask.Flask(__name__)
UPLOAD_FOLDER = 'MC_images'

@app.route('/', methods = ['GET', 'POST'])
@app.route('/upload', methods = ['GET', 'POST'])
def handle_request():
    if flask.request.method == 'POST':
        if 'image' not in flask.request.files:
            flash('No image uploaded')
            return redirect(flask.request.url)
        
        imagefile = flask.request.files['image']
        imageCategory = flask.request.form['category']

        target_folder = f"{UPLOAD_FOLDER}/{imageCategory}"
        print(target_folder)
        if not os.path.isdir(target_folder):
            os.makedirs(target_folder)

        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save(os.path.join(target_folder, filename)) 

        return "Image upload success!"
    else:
        return 'Testing GET'

app.run(host="0.0.0.0", port=5000, debug=True)