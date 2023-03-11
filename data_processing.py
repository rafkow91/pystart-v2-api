import pandas as pd
 

data = pd.read_csv('./result.csv', delimiter=';', quotechar='"', usecols=['Name', 'SalaryMin', 'SalaryMax', 'Remote', 'TechnologyStack', 'URL', 'ContractType'])
data.URL.drop_duplicates(inplace=True)
data['SalaryAvg'] = (data.SalaryMin + data.SalaryMax)/2

b2b = data[data.ContractType == 'b2b']

permament = data[data.ContractType == 'permament']

mandate_contract = data[data.ContractType == 'mandate_contract']


python_dict = {
    'all_contracts_types': {
        'min': round(data.SalaryMin.min()/160, 2),
        'max': round(data.SalaryMax.max()/160, 2),
        'mean': round(data.SalaryAvg.mean()/160, 2),
        'offers': len(data),
        'offers_without_salary': len(data[data.SalaryMin.isnull()])

    }, 
    'b2b': {
        'min': round(b2b.SalaryMin.min()/160, 2),
        'max': round(b2b.SalaryMax.max()/160, 2),
        'mean': round(b2b.SalaryAvg.mean()/160, 2),
        'offers': len(b2b),
        'offers_without_salary': len(b2b[data.SalaryMin.isnull()])
    },
    'permament': {
        'min': round(permament.SalaryMin.min()/160, 2),
        'max': round(permament.SalaryMax.max()/160, 2),
        'mean': round(permament.SalaryAvg.mean()/160, 2),
        'offers': len(permament),
        'offers_without_salary': len(permament[data.SalaryMin.isnull()])
    },
    'mandate_contract': {
        'min': round(mandate_contract.SalaryMin.min()/160, 2),
        'max': round(mandate_contract.SalaryMax.max()/160, 2),
        'mean': round(mandate_contract.SalaryAvg.mean()/160, 2),
        'offers': len(mandate_contract),
        'offers_without_salary': len(mandate_contract[data.SalaryMin.isnull()])
    }, 
}