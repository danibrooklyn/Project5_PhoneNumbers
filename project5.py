import pandas as pd

# Чтение файла Excel
df = pd.read_excel('phone_numbers.xlsx')
# Очистка телефонных номеров от ненужных символов
df['Phone Numbers'] = df['Phone Numbers'].str.replace(r'\D', regex=True)
# Сохранение результатов в новый файл Excel 
df.to_excel('cleaned_phone_numbers.xlsx',
index=False)

