MODEL_NAME="lightGBM.pkl"
VERSION_NUMBER=0.1

MODEL_DIRCTORY="model"

FINAL_COLUMNS=['Age',
               'RoomService',
               'FoodCourt',
               'ShoppingMall',
               'Spa',
               'VRDeck',
               'HomePlanet',
               'CryoSleep',
               'Destination',
               'VIP']

POST_PROCESSING=['Age', 'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck',
       'HomePlanet_Earth', 'HomePlanet_Europa', 'HomePlanet_Mars',
       'CryoSleep_False', 'CryoSleep_True', 'Destination_55 Cancri e',
       'Destination_PSO J318.5-22', 'Destination_TRAPPIST-1e', 'VIP_False',
       'VIP_True']


IMPUTER={
    "HomePlanet": "Earth",
    "CryoSleep": False,
    "Destination":"TRAPPIST-1e",
    "VIP":False,
    'Age': 28.82793046746535,
    'RoomService': 224.687617481203,
    'FoodCourt': 458.07720329024676,
    'ShoppingMall': 173.72916912197996,
    'Spa': 311.1387779083431,
    'VRDeck': 304.8547912992357
}

ONE_HOT_VECTOR={
    "HomePlanet":
        {
            'Earth':[1,0,0],
            'Europa':[0,1,0],
            'Mars':[0,0,1]
         },
    "CryoSleep":{
        False : [1,0],
        True : [0,1]
    },
    "VIP":{
        False : [1,0],
        True : [0,1]
    },
    "Destination":{
        '55 Cancri e':[1,0,0],
        'PSO J318.5-22':[0,1,0],
        'TRAPPIST-1e': [0,0,1]
    }
}