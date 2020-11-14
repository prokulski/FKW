import tabula
import pandas as pd

pdf_file = "lista_beneficjentow20201113.pdf"

table = tabula.read_pdf(pdf_file, pages="all", pandas_options={'header': None})

table_full = pd.concat(table)
table_full.drop([0, 1], axis=0, inplace=True)
table_full.columns = ['nazwa_jednostki', 'kwota_wsparcia']
table_full['kwota_wsparcia'] = table_full['kwota_wsparcia'].apply(lambda s: int(s.replace(' zł', '').replace(' ', '')))

table_full.to_csv("lista_beneficjentow.csv", index=False)
