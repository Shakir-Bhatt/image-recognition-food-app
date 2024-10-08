# Use TensorFlow image as base
FROM tensorflow/tensorflow:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to install dependencies
COPY requirements.txt .

# Install Flask and other dependencies (TensorFlow is already installed)
RUN pip install --no-cache-dir Flask==2.0.1 requests==2.26.0

# Copy the application code into the container
# This should ensure files are in the correct locations
COPY ./app /app
COPY ./static /app/static
COPY ./templates /app/templates

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "/app/app.py"]