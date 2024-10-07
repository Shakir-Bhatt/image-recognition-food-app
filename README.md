# Fruit & Vegetable Image Recognition and Nutritional Information

This project is a simple web application that allows users to upload an image of a fruit or vegetable. The application recognizes the item in the image using a pre-trained machine learning model (MobileNetV2) and fetches its nutritional value from the **Nutritionix API**.

## Features

- Upload an image of a fruit or vegetable.
- Recognize the fruit/vegetable using a pre-trained machine learning model.
- Retrieve real-time nutritional information (calories, protein, carbs, etc.) from the **Nutritionix API**.

## Project Structure

### Create container image
 `docker build -t image-recognition-food-app .`
### Run docker image
 `docker run -p 5500:5000 image-recognition-food-app`