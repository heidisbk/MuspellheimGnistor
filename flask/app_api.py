from flask import Flask, render_template, request
import warnings
import urllib.request
import requests, time

warnings.filterwarnings('ignore')

def date_time():
    day = time.localtime().tm_mday
    month = time.localtime().tm_mon
    year = time.localtime().tm_year
    return f'{day}/{month}/{year}'

date = date_time()
app = Flask(__name__)



# Page d'acceuil
@app.route('/', methods=['GET'])
def app_home():
    return render_template("index.html", date=date)



# Page d'action
@app.route('/submit/', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        path = "./static/assets/img.jpg"
        try:
            img_url = request.form['input_text']
            # urllib.request.urlretrieve(img_url, path)

            # response = requests.get('https://muspellheim-api.azurewebsites.net/predict', params={'img_url': img_url}).json()
            response = requests.get('http://127.0.0.1:8000/predict', params={'img_url': img_url}).json()

            print(response)

            return render_template("submit.html", img=img_url,
                                   prediction=response['Prediction'],
                                   accuracy=response['Probabilité'])
        except:
            return render_template("submit.html")

if __name__ == '__main__':
    app.run()
