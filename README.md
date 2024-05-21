# Chui

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


```sh
python src/run.py
```

Ensure you have below in a .env file at the root of chui
```sh
client_id
secret_key
API_HOST
```
Below are the inputs for the Endpoints
```sh
create_pdp

{
  "dataset_id" : "1b8353a1-25d1-41db-9088-f6477d4eaa17",
  "column_name" : "Attending",
  "values" : ["TRUE"],
  "pdp_name": "Risasi imebaki jamo",
  "users":[1180485267],
  "groups":[]

}
```

```sh
copy_pdp

{
  "existing_dataset_id" : "1b8353a1-25d1-41db-9088-f6477d4eaa17",
  "new_dataset_id" : "51c51ad3-44e0-46be-8456-031c51794dd8"
}
```
