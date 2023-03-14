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
