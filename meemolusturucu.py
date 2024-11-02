# İçeri Aktar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form sonuçları 
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # seçilen resmi almak
        selected_image = request.form.get('image-selector')

        # Görev #2. Metni almak
        TextTop = request.form.get("textTop")
        TextBottom = request.form.get("textBottom")

        # Görev #3. Metnin konumunu almak
        TextTop_y = request.form.get("textTop_y")
        TextBottom_y = request.form.get("textBottom_y")


        # Görev #3. Metnin rengini almak
        

        return render_template('index.html', 
                               # Seçilen resmi görüntüleme
                               selected_image=selected_image, 

                               # Görev #2. Metni görüntüleme
                               TextTop = TextTop,
                               TextBottom = TextBottom,

                               # Görev #3. Rengi görüntüleme
                               
                               
                               # Görev #3. Metnin konumunu görüntüleme
                                TextTop_y = TextTop_y,
                                TextBottom_y = TextBottom_y

                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
