# python-part8
Learning python part 8

To create the virtual env

```sh
pipenv install
``````

To activate

```sh
pipenv shell
``````

To run 

```sh
pipenv run python app.py
``````

Curl to send data

```sh
curl -X POST -F 'title=my new title' -F 'content=my new content' http://127.0.0.1:5000/post/create
``````