#Build and run the docker image locally

#docker buildx build --platform linux/amd64 -t name-ynov-mlflow .
#docker build . -t name-ynov-mlflow

docker run -it\
 -p 500:500\
 -v "$(pwd):/home/app"\
 -e PORT=500\
 -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID\
 -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY\
 -e BACKEND_STORE_URI=$BACKEND_STORE_URI\
 -e ARTIFACT_STORE_URI=$ARTIFACT_STORE_URI name-ynov-mlflow