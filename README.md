# AdidasInterViewProduction
### Objective

1. This is a raw notebook and expectation is to make it a production ready.
2. Convert this into a git project and deliver as your github repo
3. Dockerize the project for build and execution
4. Build CI pipeline using jenkins (optional, can also picked during discussion)

### Completed
- [X] This is a raw notebook and expectation is to make it a production ready.
- [X] Convert this into a git project and deliver as your github repo
- [X] Dockerize the project for build and execution
- [ ] Build CI pipeline using jenkins (optional, can also picked during discussion)

### Project Structure

    ├── app
    │   ├── config
    │   │   ├── config.py
    │   ├── model
    │   │   ├── *.pkl
    │   ├── script
    │   │   ├── model_loader.py
    │   │   ├── preprocess.py
    │   ├── app.py
    ├── Dockerfile
    ├── requirement.txt
    └── .gitignore


### Details on Complted task
##### 1. This is a raw notebook and expectation is to make it a production ready.
The productionization was done using API based production methodology



To make the above mentioned notebook the following steps are taken

- The model in the notebook(LightGBM) is saved into pickle file in `model` Folder
- The preprocesing `preprocess.py` in `scripts` preprocess the data 
    - Imputation: The null values from the user is imputed, the data is imputed w.r.t to notebook. What is meant by that is the imputation parameters are static in nature.The imputation data is in `config.py`
    - OneHotEncoding: There are 4 valiables with categorical data namely 'HomePlanet', 'CryoSleep', 'VIP', 'Destination'. The categories are also saved in `config.py`. 
- `model_loader.py` in `scripts` is used to load the model and provide prediction.
**note** the best practice is to load the model once and predict n number of times.
- `MODEL_NAME` and `FOLDER_DETAILS` are also saved in `config.py`
- `app.py` is the main file for the flask application


###### *Points of improvemnet in the notebook
- The ML notebook for OneHotEncoding should have used the OneHotEncoder scikit-learn module,that would help in deployment scenerios
- Model version tracking and performance tracking at development lifecycle should be present as most of the models are iterative in nature


##### 2. Convert this into a git project and deliver as your github repo
The following is put into github as a public repo
```
git clone https://github.com/neelindresh/AdidasInterViewProduction.git
```
##### 3. Dockerize the project for build and execution
`Dockerfile` in the repo can be used to build a container for the model.

To build the docker image
```
docker build --tag python-adidas .
```
To run the image
```
docker run -d -p 5005:5005 python-adidas
```

Then you can open localhost or server at port `5005` to get access to the web app


### How to get model predictions?

###### Sample Input
`sample.json`
```
[{
    "PassengerId": "0001_01",
    "HomePlanet": "Europa",
    "CryoSleep": false,
    "Cabin": "B/0/P",
    "Destination": "TRAPPIST-1e",
    "Age": 39.0,
    "VIP": false,
    "RoomService": 0.0,
    "FoodCourt": 0.0,
    "ShoppingMall": 0.0,
    "Spa": 0.0, 
    "VRDeck": 0.0, 
    "Name": "Maham Ofracculy", 
    "Transported": false
}, {
    "PassengerId": "0002_01",
     "HomePlanet": "Earth", 
     "CryoSleep": false, 
     "Cabin": "F/0/S", 
     "Destination": "TRAPPIST-1e", 
     "Age": 24.0, 
     "VIP": false, 
     "RoomService": 109.0, 
     "FoodCourt": 9.0, 
     "ShoppingMall": 25.0, 
     "Spa": 549.0, 
     "VRDeck": 44.0, 
     "Name": "Juanna Vines", 
     "Transported": true
}, {
    "PassengerId": "0003_01", 
    "HomePlanet": "Europa", 
    "CryoSleep": false, 
    "Cabin": "A/0/S", 
    "Destination": "TRAPPIST-1e", 
    "Age": 58.0, 
    "VIP": true, 
    "RoomService": 43.0, 
    "FoodCourt": 3576.0, 
    "ShoppingMall": 0.0, 
    "Spa": 6715.0, 
    "VRDeck": 49.0, 
    "Name": "Altark Susent", 
    "Transported": false
}, {
    "PassengerId": "0003_02", 
    "HomePlanet": "Europa", 
    "CryoSleep": false, 
    "Cabin": "A/0/S", 
    "Destination": "TRAPPIST-1e", 
    "Age": 33.0, 
    "VIP": false, 
    "RoomService": 0.0, 
    "FoodCourt": 1283.0, 
    "ShoppingMall": 371.0, 
    "Spa": 3329.0, 
    "VRDeck": 193.0, 
    "Name": "Solam Susent", 
    "Transported": false
}, {
    "PassengerId": "0004_01", 
    "HomePlanet": "Earth", 
    "CryoSleep": false, 
    "Cabin": "F/1/S", 
    "Destination": "TRAPPIST-1e", 
    "Age": 16.0, 
    "VIP": false, 
    "RoomService": 303.0, 
    "FoodCourt": 70.0, 
    "ShoppingMall": 151.0, 
    "Spa": 565.0, "VRDeck": 2.0, 
    "Name": "Willy Santantines", 
    "Transported": true}
]
```
Code snippet for converting a dataframe to the given format
```python
import json
records=df[:5].to_dict('records')
json.dump(records,open("example.json","w"))
```
###### Sample Output
```json
{
    "predictions": [
        "True",
        "False",
        "False",
        "False",
        "False"
    ]
}
```

#### Getting the predictions

Using python
```python
import requests
import json
url="http://localhost:5005/"
sample=json.load(open("sample.json"))

r=requests.post(url,json=sample)

print(r.content)
```

### Points of improvement in the while case study
- CI/CD pipeline
- Model monitering and version control
- Data Drift monitering
- Production stategy impementation
    - version based model production
    - Blue-Green deployment
    - Canary deployment

