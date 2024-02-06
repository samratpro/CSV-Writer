import chardet
import pandas as pd

def detect_encoding(file_name):
    with open(file_name, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

def csv_to_dict(file_name):
    encoding = detect_encoding(file_name)
    df = pd.read_csv(file_name, encoding=encoding)
    # df = pd.read_excel(file_name, encoding=encoding)
    data_dict = df.to_dict(orient='records')
    return data_dict

file_name = '/content/datasv.csv'
data_dict = csv_to_dict(file_name)

# Accessing data using column names (CSV headers)
for row in data_dict[:5]:
    print(row['Filo'])
