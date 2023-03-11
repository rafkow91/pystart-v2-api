from fastapi import FastAPI
import os
from data_processing import python_dict
from datetime import datetime, date




app = FastAPI()

juniors_earnings = {
    'date_last_update': datetime.fromtimestamp(os.path.getmtime('./result.csv')).date(),
    'python': python_dict,
}

@app.get('/pystart-api')
async def get_juniors_earnings():
    return juniors_earnings