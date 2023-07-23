''' Script for preparing data for present in API '''
from datetime import timedelta, datetime
import pandas as pd

#pylint: disable=line-too-long, inconsistent-return-statements

def prepare_output(dataframe: pd.DataFrame = None, contract_type: str = None) -> dict:
    '''
    Prepare the output dictionary.

    Parameters
    ----------
    dataframe : pd.DataFrame, optional
        The DataFrame to use. Defaults to `None`.
    contract_type : str, optional
        The contract type to filter the DataFrame by. Defaults to `None`.

    Returns
    -------
    dict
        A dictionary with the following keys:

        * min: The minimum salary.
        * max: The maximum salary.
        * mean: The mean salary.
        * offers: The number of offers.
        * offers_without_salary: The number of offers without salary.

    Raises
    ------
    KeyError
        If the contract type is not `None` and the DataFrame does not contain any offers for that contract type.
    '''
    if dataframe is not None:
        data = dataframe[dataframe.ContractType ==
                         contract_type] if contract_type is not None else dataframe
        if len(data) > 0:
            not_only_nan = len(data) > len(data[data.SalaryMin.isnull()])
            return {
                'min': round(data.SalaryMin.min()/160, 2) if not_only_nan else None,
                'max': round(data.SalaryMax.max()/160, 2) if not_only_nan else None,
                'mean': round(data.SalaryAvg.mean()/160, 2) if not_only_nan else None,
                'offers': len(data),
                'offers_without_salary': len(data[data.SalaryMin.isnull()])
            }


def check_result_file(path: str = './result.csv', delimiter: str = ';', quotechar: str = '"', usecols: list = None, days: int = 10):
    '''
    Check the result file and return a dictionary with the results.

    Parameters
    ----------
    path : str, optional
        The path to the result file. Defaults to `./result.csv`.
    delimiter : str, optional
        The delimiter used in the result file. Defaults to `;`.
    quotechar : str, optional
        The quote character used in the result file. Defaults to `"`.
    usecols : list, optional
        A list of columns to use from the result file. Defaults to `['Name', 'SalaryMin', 'SalaryMax', 'Remote', 'TechnologyStack', 'URL', 'ContractType', 'DateOfAdd']`.
    days : int, optional
        The number of days to filter the results by. Defaults to 10.

    Returns
    -------
    dict
        A dictionary with the following keys:

        * all_contracts_types: The results for all contract types.
        * b2b: The results for B2B contracts.
        * permament: The results for permanent contracts.
        * mandate_contract: The results for mandate contracts.

    Raises
    ------
    FileNotFoundError
        If the result file does not exist.
    '''
    if not usecols:
        usecols = ['Name', 'SalaryMin', 'SalaryMax', 'Remote',
                   'TechnologyStack', 'URL', 'ContractType', 'DateOfAdd']
    data = pd.read_csv(path, delimiter=delimiter,
                       quotechar=quotechar, usecols=usecols)
    data.drop_duplicates(inplace=True, subset=[
                         'Name', 'SalaryMin', 'SalaryMax', 'Remote', 'TechnologyStack', 'URL', 'ContractType'], keep='last')
    data['SalaryAvg'] = (data.SalaryMin + data.SalaryMax)/2
    filter_by_date = data.DateOfAdd.apply(
        pd.to_datetime) > datetime.now() - timedelta(days=days)
    data = data[filter_by_date]

    if len(data) > 0:
        python_dict = {
            'all_contracts_types': prepare_output(data),
            'b2b': prepare_output(data, 'b2b'),
            'permament': prepare_output(data, 'permament'),
            'mandate_contract': prepare_output(data, 'mandate_contract'),
        }
    else:
        python_dict = {
            'error': 'out_of_date'
        }

    return python_dict
