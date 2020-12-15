### Copy the project in your local directory

git clone https://github.com/sandrohr95/API-Example-Salud.git

Before running `API-Example-Salud`, insert your own values in `.env` . 

`API-Example-Salud` will look for a valid `.env` file in the **current working directory**.
 In its absence, it will use environmental variables (environment variables will always take priority over values loaded from a dotenv file).

### 🚀 Setup 

#### Installation

In order to install all the packages needed to deploy the API via source code:

```console
$ python setup.py install
```

#### Deploy server 

Server can be [deployed](https://fastapi.tiangolo.com/deployment/) with *uvicorn*, a lightning-fast ASGI server, using the command-line client.
```
RUN app.py file
```

This api has been nade with FastAPI. Fastapi provides swagger documentation automatically in url http://localhost:8080/api/docs. Here you can test the API methods without having to implement an interface.

Online documentation is available at `http://localhost:8080/api/docs`.
