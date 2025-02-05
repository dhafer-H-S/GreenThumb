# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
from utils.disease import disease_dic
from utils.fertilizer import fertilizer_dic
import requests
import pickle
import io
import torch
from torchvision import transforms
from PIL import Image
from utils.model import ResNet9
# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading plant disease classification model

disease_classes = ['Apple___Apple_scab',
                   'Apple___Black_rot',
                   'Apple___Cedar_apple_rust',
                   'Apple___healthy',
                   'Blueberry___healthy',
                   'Cherry_(including_sour)___Powdery_mildew',
                   'Cherry_(including_sour)___healthy',
                   'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                   'Corn_(maize)___Common_rust_',
                   'Corn_(maize)___Northern_Leaf_Blight',
                   'Corn_(maize)___healthy',
                   'Grape___Black_rot',
                   'Grape___Esca_(Black_Measles)',
                   'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Grape___healthy',
                   'Orange___Haunglongbing_(Citrus_greening)',
                   'Peach___Bacterial_spot',
                   'Peach___healthy',
                   'Pepper,_bell___Bacterial_spot',
                   'Pepper,_bell___healthy',
                   'Potato___Early_blight',
                   'Potato___Late_blight',
                   'Potato___healthy',
                   'Raspberry___healthy',
                   'Soybean___healthy',
                   'Squash___Powdery_mildew',
                   'Strawberry___Leaf_scorch',
                   'Strawberry___healthy',
                   'Tomato___Bacterial_spot',
                   'Tomato___Early_blight',
                   'Tomato___Late_blight',
                   'Tomato___Leaf_Mold',
                   'Tomato___Septoria_leaf_spot',
                   'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Target_Spot',
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                   'Tomato___Tomato_mosaic_virus',
                   'Tomato___healthy']

disease_model_path = 'models/plant_disease_model.pth'
disease_model = ResNet9(3, len(disease_classes))
disease_model.load_state_dict(torch.load(
    disease_model_path, map_location=torch.device('cpu')))
disease_model.eval()


# Loading crop recommendation model

crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


# =========================================================================================

# Custom weather functions for calculations


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    base_url = "http://api.weatherapi.com/v1/current.json?key=b93150bd06e74250992224305252301&q=tunisia&aqi=yes"

    complete_url = base_url
    response = requests.get(complete_url)
    x = response.json()

    if "error" not in x:
        current = x["current"]
        temperature = current["temp_c"]
        humidity = current["humidity"]
        return temperature, humidity
    else:
        return None


def predict_image(img, model=disease_model):
    """
    Transforms image to tensor and predicts disease label
    :params: image
    :return: prediction (string)
    """
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.ToTensor(),
    ])
    image = Image.open(io.BytesIO(img))
    img_t = transform(image)
    img_u = torch.unsqueeze(img_t, 0)

    # Get predictions from model
    yb = model(img_u)
    # Pick index with highest probability
    _, preds = torch.max(yb, dim=1)
    prediction = disease_classes[preds[0].item()]
    # Retrieve the class label
    return prediction

# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Smart Farming, Bright Future - Home'
    return render_template('index.html', title=title)

# render crop recommendation form page


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Smart Farming, Bright Future - Crop Recommendation'
    return render_template('crop.html', title=title)

# render fertilizer recommendation form page


@ app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'Smart Farming, Bright Future - Fertilizer Suggestion'

    return render_template('fertilizer.html', title=title)

# render disease prediction input page




# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page


@app.route('/crop-predict', methods=['GET', 'POST'])
def crop_prediction():
    title = 'Smart Farming, Bright Future - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        city = request.form.get("city")

        if weather_fetch(city) is not None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            return render_template('crop-result.html', prediction=final_prediction, title=title)
        else:
            return render_template('try_again.html', title=title)
    else:
        return render_template('crop.html', title=title)

# render fertilizer recommendation result page


@app.route('/fertilizer-predict', methods=['GET', 'POST'])
def fertilizer_recommend():
    title = 'Smart Farming, Bright Future - Fertilizer Suggestion'

    crop_name = str(request.form['cropname'])
    N = int(request.form['nitrogen'])
    P = int(request.form['phosphorous'])
    K = int(request.form['pottasium'])

    df = pd.read_csv('Data-processed/fertilizer.csv')

    plant_data = df[df['Crop'] == crop_name]

    if plant_data.empty:
        error = f"No data available for the selected crop: {crop_name}"
        return render_template('fertilizer-result.html', error=error, title=title)

    nr = plant_data['N'].iloc[0]
    pr = plant_data['P'].iloc[0]
    kr = plant_data['K'].iloc[0]

    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"

    response = Markup(str(fertilizer_dic[key]))

    return render_template('fertilizer-result.html', recommendation=response, title=title)
# render disease prediction result page


@app.route('/disease-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = 'Smart Farming, Bright Future - Disease Detection'

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return render_template('disease.html', title=title)
        try:
            img = file.read()

            prediction = predict_image(img)

            prediction = Markup(str(disease_dic[prediction]))
            return render_template('disease-result.html', prediction=prediction, title=title)
        except:
            pass
    return render_template('disease.html', title=title)

#-----------------------------------Crop recommendation based on input--------------------------------------------------------
# extract crop name from fertilizer csv file
def get_crops():
    df = pd.read_csv('Data-processed/recommendation.csv')
    return df['Crop'].tolist()

def get_best_conditions(plant):
    """
    Returns the best conditions for a given plant
    :params: plant
    :return: conditions (dict)
    """
    df = pd.read_csv('Data-processed/recommendation.csv')
    df['Crop'] = df['Crop'].astype(str)  # Ensure the Crop column contains only string values

    plant_data = df[df['Crop'].str.lower() == plant.lower()]

    if plant_data.empty:
        return None

    plant_data = plant_data.iloc[0]

    # Extract the optimal conditions from the dataset
    conditions = {
        'Crop': plant_data['Crop'],
        'N': plant_data['N'],
        'P': plant_data['P'],
        'K': plant_data['K'],
        'pH': plant_data['pH'],
        'Soil_Moisture': plant_data['Soil_Moisture'],
        'Temperature': plant_data['Temperature'],
        'Light_Condition_Advice': plant_data['Light_Condition_Advice'],
        'Rainfall_or_Preferred_Watering': plant_data['Rainfall_or_Preferred_Watering'],
    }
    return conditions

# Add this route to render the plant recommendation form page
@app.route('/plant-recommend')
def plant_recommend():
    title = 'Smart Farming, Bright Future - Plant Recommendation'
    crops = get_crops()
    return render_template('plant.html', title=title, crops=crops)

@app.route('/plant-recommendation', methods=['GET', 'POST'])
def plant_recommendation():
    title = 'Smart Farming, Bright Future - Plant Recommendation'
    if request.method == 'POST':
        plant = request.form['plant']
        city = request.form['city']
        state = request.form['state']

        # Fetch the best conditions for the selected plant
        conditions = get_best_conditions(plant)

        if conditions is None:
            error = f"No data available for the selected plant: {plant}"
            return render_template('plant-result.html', error=error, title=title)

        # Fetch the current weather conditions for the user's city
        weather = weather_fetch(city)
        if weather is not None:
            current_temperature, current_humidity = weather
            current_conditions = f"Current conditions in {city}, {state}: Temperature {current_temperature}°C, Humidity {current_humidity}%"
        else:
            current_conditions = f"Weather data not available for {city}, {state}"

        return render_template('plant-result.html', conditions=conditions, current_conditions=current_conditions, title=title)
    else:
        crops = get_crops()
        return render_template('plant.html', title=title, crops=crops)
#--------------------------------------------------------------------------------------------
# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)

