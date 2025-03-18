# Use an official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install flask pymongo

# Expose Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
