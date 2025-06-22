# Base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose Django default port
EXPOSE 8000

# Run the app (adjust `manage.py` path if needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
