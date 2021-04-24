# FastAPI

![Python](https://img.shields.io/badge/python-3.8-brightgreen.svg)
![FastApi](https://img.shields.io/badge/fastapi-0.63-orange.svg)

A simple-sample *FastAPI* application with examples of `POST`, `GET` and `PUT` requests.


## Running Locally

**Dependencies**

- python `3.8`
- fast-api `0.63.0`

**Building the Environment**

Create new environment:
`conda env create --file source/environment.yml`

Activate the environment you just created:
`source activate fast-api`

If you want to deactivate the environment:
`conda deactivate`

To run the App:
```
cd source
uvicorn main:app --reload
```

## Using the APP

Run: `http://127.0.0.1:8000/users/9?q=test`

To check the Swagger/OpenAPI: `http://127.0.0.1:8000/docs#/`

**GET Request**
```
curl -X 'GET' \
  'http://127.0.0.1:8000/users/123456789?q=test' \
  -H 'accept: application/json'
```

**PUT Request**
```
curl -X 'PUT' \
  'http://127.0.0.1:8000/users/123456789' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "anna",
  "dateOfBirth": "10-10-2020",
  "is_current": true
}'
```

**POST Request**
```
curl -X 'POST' \
  'http://127.0.0.1:8000/medias?phrase=I%20like%20dogs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "anna",
  "date": "14-04-2021"
}'
```

**References**

- [FastAPI](https://fastapi.tiangolo.com/)
