# heroku container:login

# heroku create heidi-ynov-flask 

# docker buildx build --platform linux/amd64 -t heidi-ynov-flask  .

docker build . -t heidi-ynov-flask

docker tag heidi-ynov-flask  registry.heroku.com/heidi-ynov-flask/web

docker push registry.heroku.com/heidi-ynov-flask/web

heroku container:release web -a heidi-ynov-flask 

heroku open -a heidi-ynov-flask
