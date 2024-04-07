# Python Flask Backend

I tried to follow best-practices regarding structuring the project. The endpoint implementations can be found in app/resources/tv_show_resources.py

## Requirements

- Python 3.10.12

Please use a virtual environment.

Install required packages:
```bash
pip install -r requirements.txt
```

You should also create a .env file with the following content:
(I am aware that we should not put .env content somewhere public, but it is required for this to run and it does not contain anything sensitive. But should be avoided nevertheless.)
```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///tvshows.db
```

To start the server, please run the following command:
```bash
python run.py
```

To start unittest (run in root folder directory). The server should be running before unittesting!:
```bash
python -m unittest tests/test_app.py
```

## Description
This service supports the following endpoints:
- Create a new TV show.
    - Method: POST
    - Endpoint: /tvshows
    - Headers: Content-Type - application/json
    - Body: raw JSON
- Retrieve all TV shows.
    - Method: GET
    - Endpoint: /tvshows
- Retrieve a single TV show by its ID. 
    - Method: GET
    - Endpoint: /tvshows/{id}
- Search TV show by genre.
    - Method: GET
    - Endpoint: /tvshows/search/{genre}
- Update an exisCng TV show.
    - Method: PUT
    - Endpoint: /tvshows/{id}
    - Headers: Content-Type - application/json
    - Body: raw JSON
- Delete a TV show by its ID.
    - Method: DELETE
    - Endpoint: /tvshows/{id}


When adding new TV shows, the id of the show gets incremented automatically.

## Some notable features:
- Unittest included (testing all endpoints)
- Supports the required endpoints
- Automatic creation of local database

## Screenshots

Starting server:
![alt text](<Screenshots/Screenshot 2024-04-07 at 17.31.03.png>)

Unittest:
![alt text](<Screenshots/Screenshot 2024-04-07 at 17.31.30.png>)

Postman Create Show:
![alt text](<Screenshots/Screenshot 2024-04-07 at 17.32.29.png>)

Postman Retrieve All Shows:
![alt text](<Screenshots/Screenshot 2024-04-07 at 17.34.52.png>)

Postman Retrieve Show by ID:
![alt text](<Screenshots/Screenshot 2024-04-07 at 17.37.03.png>)

Postman Search TV Show by Genre:
![alt text](<Screenshots/Screenshot 2024-04-07 at 17.40.28.png>)

Postman Update Show by ID:
![alt text](<Screenshots/Screenshot 2024-04-07 at 17.41.29.png>)

Postman Delete Show by ID:
![alt text](<Screenshots/Screenshot 2024-04-07 at 17.41.45.png>)

Server Output:
![alt text](<Screenshots/Screenshot 2024-04-07 at 17.41.59.png>)


