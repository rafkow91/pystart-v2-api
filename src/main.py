"""API to present earning of junior developer"""

from datetime import datetime
import os

from fastapi import FastAPI

from data_processing import check_result_file


app = FastAPI()


@app.get('/')
async def get_juniors_earnings(days: int = None):
    '''
    Get the earnings of juniors for the specified number of days.

    Parameters
    ----------
    days : int, optional
        The number of days to get the earnings for. Defaults to 10.

    Returns
    -------
    dict
        A dictionary with the following keys:

        * date_last_update: The date the result file was last updated.
        * python: The earnings of juniors for the specified number of days.

    Raises
    ------
    ValueError
        If `days` is not a positive integer.
    '''
    if days is None:
        days = 10
    return {
        'date_last_update': datetime.fromtimestamp(os.path.getmtime('./result.csv')),
        'python': check_result_file(days=int(days)),
    }
