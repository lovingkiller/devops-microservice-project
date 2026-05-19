#Pyhton offciial lightweight image use 
FROM python:3.9-slim

# Container WORKING dIRECTORY
WORKDIR /app

# cOPY REQUIREMENT AND INSTALL DEPENDENCIES
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY ALL CODE IN Container
COPY . .

#Flask default port expose
EXPOSE 5000

#Application run command 
CMD ["python", "app.py"]