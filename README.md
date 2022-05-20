# Python Backend Template

This is a template for writing backends in python with the following:

1. Flask (Routes)
2. SQLAlchemy (ORM)
3. SQLite3 (DB)

It includes a basic "hello, world!" endpoint, and a basic user model and endpoints.

## Virtualenv

Virtualenv setup!

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Running the Server

To run the server, run:

```bash
python3 src/run.py
```

The hello-world endpoint can be found at: http://127.0.0.1:5000/
