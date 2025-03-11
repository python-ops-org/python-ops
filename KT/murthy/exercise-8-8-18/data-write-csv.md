
```

import csv

file = 'test.csv'
data = [
    ["name", "score"],
    ["virat", "100"],
    ["rohit", "120"]
]

f = open(file, newline='', mode='w')  # Using your original open syntax
w = csv.writer(f)

for row in data:
    w.writerow(row)

f.close()  # Don't forget to close the file

print(f"Data written to {file}")

```


```

import csv
import datetime

# Generate timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Define file name with timestamp
file = f"test_{timestamp}.csv"

# Data to be written
data = [
    ["name", "score"],
    ["virat", "100"],
    ["rohit", "120"]
]

# Open file and write data
with open(file, newline='', mode='w', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerows(data)  # Write all rows at once

print(f"Data written to {file}")

```
