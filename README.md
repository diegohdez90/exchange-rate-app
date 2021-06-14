# Exchange Application

## How to install?

### Pre-requirements

* Python 3.9

### Install

1. Clone reposotory.
2. Install pip dependencies with.
*  `$ pip install -r requirements.txt`
* Or install dependencies using pipenv or venv environments
3. Run script `$ python -m flask run`
4. Go to browser [http://localhost:5000](http://localhost:5000)

## How it works?

In the http://localhost:5000 add the next query parameters
* from. Currency three codes you would like to convert from.
* to. Currency three codes you would like to convert to.

i.e. http://localhost:5000?from=USD&to=MXN means convert $1 USD in MXN.
