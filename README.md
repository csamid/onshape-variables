# Onshape's Variables API Helper

A python class to easily interact with Onshape's Variables API 

## Prerequisites

#### Create API Keys
- Head over to the onshape [developer portal](https://dev-portal.onshape.com/keys) 

- Click on "Create new API key"

![new_keys](./assets/new_key.png)

- Check the blue boxes and click on "Create API key"

![create_keys](./assets/create_key.png)

- copy and save both keys in a file (I recommend you save it in a [.env file](./examples/.env.example). What is a .env? See this [article](https://www.atatus.com/blog/python-environment-variables/#what-are-environment-variables)!)

![save_keys](./assets/save_keys.png)

## Installation

You can install onshape-variables via pip:

```bash
pip install onshape-variables
```

## Usage

```python
from onshape_variables.variables import Variables

# create variables object
my_vs = Variables(api_keys, did, wid)

# create a varaible studio 
my_vs.create_varaible_studio(name="My Varaible Studio")
```

[Check out the example notebook](./examples/example.ipynb)

Also see [Onshape's documentation](https://onshape-public.github.io/docs/) and [API explorer](https://cad.onshape.com/glassworks/explorer/#/)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change :)


<!-- ## License

[MIT](https://choosealicense.com/licenses/mit/) -->