''' Script for preparing data for present in API '''
from datetime import timedelta, datetime
import pandas as pd

# todo: fill the docstrings for functions
def prepare_output(dataframe: pd.DataFrame = None, contract_type: str = None) -> dict:
    '''
    _summary_

    Keyword Arguments:
        dataframe -- _description_ (default: {None})
        contract_type -- _description_ (default: {None})

    Returns:
        _description_
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
    return None


def check_result_file(path: str = './result.csv', delimiter: str = ';', quotechar: str = '"', usecols: list = None, days: int = 10):
    '''
    _summary_

    Keyword Arguments:
        path -- _description_ (default: {'./result.csv'})
        delimiter -- _description_ (default: {';'})
        quotechar -- _description_ (default: {'"'})
        usecols -- _description_ (default: {None})
        days -- _description_ (default: {10})

    Returns:
        _description_
    '''
    if not usecols:
        usecols = ['Name', 'SalaryMin', 'SalaryMax', 'Remote',
                   'TechnologyStack', 'URL', 'ContractType', 'DateOfAdd']
    data = pd.read_csv(path, delimiter=delimiter,
                       quotechar=quotechar, usecols=usecols)
    data.drop_duplicates(inplace=True, keep='last')
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
