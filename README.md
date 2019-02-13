# sample-docker-application


## To run the application 
#### Step 1: create a docker image (one time process)
	docker build -f docker/Dockerfile -t docker-calix-flask:latest .

#### Step 2: run the docker image
	docker run --name flaskapp -v$PWD/flask-service:/flask-service -p5000:5000 docker-calix-flask:latest

#### Step 3: on your fav browser open the link 
	http://localhost:5000/say_hello/<name>

