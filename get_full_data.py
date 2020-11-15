import pandas as pd
import simplejson as json

from utils.utils import api_search

wykaz = pd.read_csv('lista_beneficjentow.csv')

full_df = pd.DataFrame()

for row in wykaz.iterrows():
    entry = row[1]['nazwa_jednostki']

    print(entry)

    response = api_search(entry)
    response_json = json.loads(response.content)

    if response_json.get('total') > 0:
        for item in response_json.get('items'):

            temp_df = {}

            temp_df['entry'] = entry
            temp_df['address_city'] = item.get('address').get('city')
            temp_df['address_code'] = item.get('address').get('code')
            if item.get('ceo'):
                temp_df['ceo_name'] = item.get('ceo').get('name')
            temp_df['first_entry_date'] = item.get('first_entry_date')
            temp_df['krs'] = item.get('krs')
            temp_df['legal_form'] = item.get('legal_form')
            temp_df['name'] = item.get('name')
            temp_df['name_short'] = item.get('name_short')
            temp_df['nip'] = item.get('nip')
            temp_df['regon'] = item.get('regon')

            industries = []
            if item.get('industries'):
                for i in item.get('industries'):
                    if i.get('main'):
                        temp_df['industries' + i.get('symbol')] = True

            full_df = full_df.append(pd.DataFrame(temp_df, index=[0]))

    full_df.to_csv('lista_beneficjentow_uzupelniona.csv', index=False)


full_df = full_df.merge(wykaz,
                        how='left',
                        left_on='entry',
                        right_on='nazwa_jednostki')
full_df.to_csv('lista_krs_dotacja.csv', index=False)
