from fastapi import FastAPI
import os
from data_processing import check_result_file
from datetime import datetime


offer_json_url = 'https://justjoin.it/api/offers'

app = FastAPI()


@app.get('/pystart-api')
async def get_juniors_earnings(days: int = None):
    if days is None:
        days = 10

    return {
        'date_last_update': datetime.fromtimestamp(os.path.getmtime('./result.csv')),
        'python': check_result_file(days=int(days)),
    }
