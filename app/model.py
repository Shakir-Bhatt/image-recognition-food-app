import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import requests

# Load pre-trained model (MobileNetV2 for example)
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Nutritionix API details
NUTRITIONIX_API_URL = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
NUTRITIONIX_API_HEADERS = {
    'x-app-id': '03d69eee',       # Replace with your Nutritionix app ID - 03d69eee
    'x-app-key': '0643f915a0628a6375f08e6792546f5b',     # Replace with your Nutritionix app key
    'Content-Type': 'application/json'
}

def predict_image(img_path):
    # Load image and preprocess
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x)

    # Make predictions
    preds = model.predict(x)
    decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)
    
    # Get top prediction (class)
    predicted_label = decoded_preds[0][0][1].lower()
    
    # Get nutritional data from Nutritionix
    nutrition_info = get_nutrition_info(predicted_label)
    
    return predicted_label, nutrition_info

def get_nutrition_info(food_item):
    """Fetch nutritional data from Nutritionix API"""
    payload = {
        'query': food_item,
        'timezone': 'US/Eastern'
    }
    response = requests.post(NUTRITIONIX_API_URL, json=payload, headers=NUTRITIONIX_API_HEADERS)
    
    if response.status_code == 200:
        nutrition_data = response.json()
        if nutrition_data['foods']:
            return nutrition_data['foods'][0]  # Return first result
    else:
        return "No nutritional data available"
