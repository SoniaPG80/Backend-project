# Base Image
FROM python:3.11.1

# Work directory
WORKDIR /hola

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy other project files
COPY . .

# Expose a port to Containers 
EXPOSE 5000

# Command to run on server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "hola:hola"]
