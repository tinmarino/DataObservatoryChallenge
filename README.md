# Quickstart

# Comments

### 1/ Patent

```bash
python3 1_patent/patent.py AAAA001  # Run program
python3 1_patent/test/test_patent.py  # Run test
```


### 2/ Starwars

```bash
python3 2_starwars/starwars.py  # Run program, getting values from files (=> no latency)
```

Note: The species are not filled in the data, so people are never considered as humans

I did not parse the iternet API every time because the website is slow here, so there are some hardcoded dictionaries and downloaded json files. But the functions to fetch and parse data from the internet are present

```python
from urllib.request import urlopen
from json import loads as json_loads, load as json_load
```

### 3/ DataEng

```bash
# Just read below
```

* Ref: https://medium.com/analytics-vidhya/pandas-csv-cheatsheet-f88abecbe289
* Ref: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

#### 3.1.1 Remove empty columns

* The first line was bad (empty => useless => deleted with vim)
* The columns tagged 'Column1' and '\_1' in the title line were empty => deleted with pandas


```python
import pandas as pd
df = pd.read_csv('test/crucero_1.csv')
empty_cols = [col for col in df.columns if df[col].isnull().all()]
df.drop(empty_cols, axis=1, inplace=True)
df.to_csv('test/crucero_3.csv')
```

* Ref: https://www.jitsejan.com/find-and-delete-empty-columns-pandas-dataframe

This created the file test/crucero_3.csv

#### 3.1.2 Check types

* Column yyyy-mm-ddThh:mm:ss.sss was not reckognised as date

```python
df['yyyy-mm-ddThh:mm:ss.sss'] = pd.to_datetime(df['yyyy-mm-ddThh:mm:ss.sss'])
```

* Ref: https://stackoverflow.com/questions/40353079/pandas-how-to-check-dtype-for-all-columns-in-a-dataframe
* Ref: https://www.geeksforgeeks.org/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/

This created the file test/crucero_4.csv

#### 3.1.3 Fill

* It was full of empty values, the diff is big

```python
df.fillna( method ='ffill', inplace = True)
```

* Ref: https://stackoverflow.com/questions/41212273/pandaspython-fill-empty-cells-with-with-previous-row-value
* Ref: Example without thinking, all at once: https://www.geeksforgeeks.org/python-pandas-dataframe-fillna-to-replace-null-values-in-dataframe/

This created the file test/crucero_5.csv

#### 3.1.4 Standard varaible

```bash
cp crucero_5.csv crucero_6.csv
vim crucero_6.csv
```

1. To lower: `gu$`
2. Replace space by underscore: `:s/ /_/g`
3. Replace non alpha num by hyphen: `:s/[^a-z0-9,]/-/g`

This created the file test/crucero_6.csv



# Tips

```python
# Dump json to file
import json
with open('data.json', 'w') as f:
    json.dump(data, f)
```
  
# Next steps

* Remove hardcode
* See IDEAS in each program main script file
* More defensive programing and expresive error messages
  * For example, the starwars jsons values are mostly are well formated fortunately
* Refactor files and create a module for each exercice
