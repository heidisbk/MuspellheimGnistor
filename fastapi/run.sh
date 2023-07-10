heroku container:login

docker build . -t 280720/muspellheim-api

docker tag 280720/muspellheim-api  registry.heroku.com/muspellheim-api/web

docker push registry.heroku.com/muspellheim-api/web

heroku container:release web -a muspellheim-api

heroku open -a muspellheim-api
