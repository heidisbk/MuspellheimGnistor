heroku container:login

#heroku create name-ynov-mlflow

#docker build -t name-ynov-mlflow .

docker buildx build --platform linux/amd64 -t name-ynov-mlflow .

docker tag name-ynov-mlflow registry.heroku.com/name-ynov-mlflow/web

docker push registry.heroku.com/name-ynov-mlflow/web

heroku container:release web -a name-ynov-mlflow

heroku open -a name-ynov-mlflow