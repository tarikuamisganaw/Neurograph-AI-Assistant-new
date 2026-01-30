FROM python:3.11-slim  
  
WORKDIR /app  
  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . ./app/  
  
ARG API_PORT
EXPOSE $API_PORT  
  
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $API_PORT"]