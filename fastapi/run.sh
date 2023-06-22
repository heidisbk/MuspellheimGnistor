# heroku container:login

# heroku create heidi-ynov-api 

# docker buildx build --platform linux/amd64 -t heidi-ynov-api  .

docker build . -t heidi-ynov-api 

docker tag heidi-ynov-api  registry.heroku.com/heidi-ynov-api/web

docker push registry.heroku.com/heidi-ynov-api/web

heroku container:release web -a heidi-ynov-api 

heroku open -a heidi-ynov-api
