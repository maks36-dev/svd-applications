from flask import Flask, render_template, request, jsonify, send_file
import os
from compress import compress_img
from utils import split_file_name


app = Flask(__name__)
UPLOAD_FOLDER = 'static/upload_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def main_page():
    return render_template('inter.html', name=__name__)


@app.route('/upload', methods=['POST'])
def upload_image():
    # check post request
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    # get file
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # save file
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        file_stat = os.stat(filename)
        file_size = file_stat.st_size / 1024**2
        return jsonify({'path': filename, "file_size": round(file_size, 3)})
    

@app.route('/compress', methods=['POST'])
def compress():
    try:
        data = request.get_json()

        perc_of_comp = int(data["perc_of_comp"]) # how many percent of the image should be leave
        name = data["name"] # name of img

        # create paths
        image_path = f'static/upload_images/{name}'
        file_name, _ = split_file_name(image_path)
        comp_img_path = f'static/compress_images/{file_name}_{perc_of_comp}.jpg'
        
        # check file in the compress folder
        if not os.path.isfile(comp_img_path):
            compress_img(image_path, perc_of_comp)

        # calculate img size
        file_stat = os.stat(comp_img_path)
        file_size = file_stat.st_size / 1024**2
        
        return jsonify({'path': comp_img_path, "file_size": round(file_size, 3)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    


if __name__ == '__main__':
    app.run(debug=True)
