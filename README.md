# Ndovu

> mtek data endpoints!

## Getting started

### Install Requirements

You can setup a virtual environnment or just be _brave_ and install the requirements

```sh
pip install -r requirements.txt
```

### Use Enviroment

On linux activate the environment as below
```sh
source env/bin/activate
```

On Windows activate the environment as below

```sh
env/Scripts/activate.bat
```

### Run the thing

```sh
python src/run.py
```

Ensure you have below in a .env file at the root of chui
```sh
Pg_conns
```
Below are the inputs for the Endpoints
```sh
load_data

[{'_id': '',
  'insurer': '',
  'stage': '',
  'clientid': '',
  '_date': {''},
  '_udate': {''},
  'product': '',
  'ModuleID': '',
  'policyStatus': ''},
 {'_id': '',
  'insurer': '',
  'stage': '',
  'clientid': '',
  '_date': {''},
  'ModuleID': '',
  '_udate': {''},
  'product': '',
  'policyStatus': ''}]
```
