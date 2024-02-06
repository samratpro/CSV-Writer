import pandas as pd
read = pd.read_excel('/content/drive/MyDrive/Rodrigue/Data-city.xlsx')
dicts = read.to_dict()

post_run = 0
i = 0
dicts_list = []
while i < len(dicts['city']):
    city = dicts['city'][post_run]
    Code_postal = dicts['Code_postal'][post_run]

    print(city)
    print(Code_postal)

    post_run += 1
    i += 1
