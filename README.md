Before running `ejemplo_4`, save a copy of [`.env.template`](.env) as `.env` and insert your own values. 

`ejemplo4` will look for a valid `.env` file in the **current working directory**.
 In its absence, it will use environmental variables (environment variables will always take priority over values loaded from a dotenv file).

### 🚀 Setup 

#### Installation

Via source code:

```console
$ python setup.py install
```

#### Deploy server 

Server can be [deployed](https://fastapi.tiangolo.com/deployment/) with *uvicorn*, a lightning-fast ASGI server, using the command-line client.
```
RUN app.py file
```

Online documentation is available at `/api/docs`.
