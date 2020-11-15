Ministerstwo Kultury przekazało na początku listopada 2020 roku dotacje dla podmiotów związanych z kulturą.

Jak to zwykle bywa - wykaz został przygotowany w pliku PDF (dobrze, że został w ogóle opublikowany). Plik ten to **listalista_beneficjentow20201113.pdf**.

Skrypt **pdf_to_csv.py** przerabia to na wersję CSV, która nadaje się do dalszej obróbki, a po zapisaniu w Excelu daje plik **lista_beneficjentow.xlsx**.

Natomiast skrypt **get_full_data.py** (po uzupełnieniu klucza api w *utils/api_key.py*) dociąga dane z KRS i całość zapisuje do **lista_krs_dotacja.csv**. Wyszukiwanie odbywa się po nazwach i nie jest najlepsze. Dlatego konieczna jest dalsza ręczna obróbka.

**BARDZO DUŻO** podmiotów nie ma w KRS, więc dla dużej liczby beneficjentów brakuje danych.

-----

Zezwalam jako autor na wykorzystanie skryptów w celach edukacyjnych. Zebrane dane pozwalam wykorzystać po wcześniejszym [kontakcie mailowym](mailto:prokulski@gmail.com).

Poza tym zapraszam na fanpage **[Dane i Analizy](https://fb.com/DaneAnalizy)** oraz **[bloga](https://blog.prokulski.science)**.
