- CSV files are a common file format for tabular data

## Reading CSVs

- **reader** - lets you iterate over rows of the CSV as lists
- **DictReader** - lets you iterate over rows of the CSV as OrderedDicts

Readers accept a delimiter kwarg in case your data isn't separated by commas.

```Python

from csv import reader
with open("example.txt") as file:
    csv_reader = reader(file,delimiter="|")
    for row in csv_reader:
        # each row is a list
        print(row)

```

## Writing to CSVs

- **writer** - creates a writer object for writing to CSV
-