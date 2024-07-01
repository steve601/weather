from flask import Flask,render_template,request
from source.main_project.pipeline.predict_pipeline import UserData,PredicPipeline

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('weather.html')

@app.route('/classify',methods=['POST'])
def do_prediction():
    data = UserData(
        temperature=request.form.get('temp'),
        humidity=request.form.get('hum'),
        wind=request.form.get('wind'),
        precipitation=request.form.get('prec'),
        cloud=request.form.get('cloud'),
        atmospheric=request.form.get('atm'),
        uv=request.form.get('uv'),
        season=request.form.get('season'),
        visibility=request.form.get('visi'),
        location=request.form.get('loc')
    )

    user_df = data.get_data_as_df()

    predition_pipe = PredicPipeline()
    result = predition_pipe.predict(user_df)

    if result == 0:
        msg = 'Weather is likely to be cloudy'
    elif result == 1:
        msg = 'Weather is likely to be rainy'
    elif result == 2:
        msg = 'Weather is likely to be sunny'
    else:
        msg = 'Weather is likely to be snowy'
        
    return render_template('weather.html',text = msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
