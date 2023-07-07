heroku container:login

docker build . -t flask_muspellheim

docker tag flask_muspellheim registry.heroku.com/muspellheim/web

docker push registry.heroku.com/muspellheim/web

heroku container:release web -a muspellheim

heroku open -a muspellheim
