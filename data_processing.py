from datetime import timedelta, datetime
import pandas as pd


def check_result_file(path: str = './result.csv', delimiter: str = ';', quotechar: str = '"', usecols: list = None, days: int = 10):
    if not usecols:
        usecols = ['Name', 'SalaryMin', 'SalaryMax', 'Remote',
                   'TechnologyStack', 'URL', 'ContractType', 'DateOfAdd']
    data = pd.read_csv(path, delimiter=delimiter,
                       quotechar=quotechar, usecols=usecols)
    data.drop_duplicates(inplace=True)
    data['SalaryAvg'] = (data.SalaryMin + data.SalaryMax)/2
    filter_by_date = data.DateOfAdd.apply(
        pd.to_datetime) > datetime.now() - timedelta(days=days)
    data = data[filter_by_date]

    if len(data) > 0:
        b2b = data[data.ContractType == 'b2b']
        if len(b2b) > 0:
            b2b_dict = {
                'min': round(b2b.SalaryMin.min()/160, 2),
                'max': round(b2b.SalaryMax.max()/160, 2),
                'mean': round(b2b.SalaryAvg.mean()/160, 2),
                'offers': len(b2b),
                'offers_without_salary': len(b2b[b2b.SalaryMin.isnull()])
            }
        else:
            b2b_dict = None

        permament = data[data.ContractType == 'permament']
        if len(permament) > 0:
            permament_dict = {
                'min': round(permament.SalaryMin.min()/160, 2),
                'max': round(permament.SalaryMax.max()/160, 2),
                'mean': round(permament.SalaryAvg.mean()/160, 2),
                'offers': len(permament),
                'offers_without_salary': len(permament[permament.SalaryMin.isnull()])
            }
        else:
            permament_dict = None

        mandate_contract = data[data.ContractType == 'mandate_contract']
        if len(mandate_contract) > 0:
            mandate_contract_dict = {
                'min': round(mandate_contract.SalaryMin.min()/160, 2),
                'max': round(mandate_contract.SalaryMax.max()/160, 2),
                'mean': round(mandate_contract.SalaryAvg.mean()/160, 2),
                'offers': len(mandate_contract),
                'offers_without_salary': len(mandate_contract[mandate_contract.SalaryMin.isnull()])
            }

        else:
            mandate_contract_dict = None

        python_dict = {
            'all_contracts_types': {
                'min': round(data.SalaryMin.min()/160, 2),
                'max': round(data.SalaryMax.max()/160, 2),
                'mean': round(data.SalaryAvg.mean()/160, 2),
                'offers': len(data),
                'offers_without_salary': len(data[data.SalaryMin.isnull()])
            },
            'b2b': b2b_dict,
            'permament': permament_dict,
            'mandate_contract': mandate_contract_dict,
        }
    else:
        python_dict = {
            'error': 'out_of_date'
        }

    return python_dict
