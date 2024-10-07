from flask import Flask, request, render_template, jsonify
from model import predict_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    # Save file and make prediction
    file_path = './uploads/' + file.filename
    file.save(file_path)
    
    predicted_label, nutrition_info = predict_image(file_path)
    
    return jsonify({
        'item': predicted_label,
        'nutrition': nutrition_info
    })

if __name__ == '__main__':
    app.run(debug=True)
