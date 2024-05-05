FROM python:3.9

# Copy the requirements file into the container
COPY app.py /app/

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
RUN pip install flask

EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
