import csv


def query_csv(file_path,rows_to_query,columns_to_query):
    try:
        with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
            data = csv.DictReader(csvfile)
            for index, row in enumerate(data, start=1):
                if index in rows_to_query:
                    selected_columns = {col: row[col] for col in columns_to_query}
                    print(selected_columns)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file = "D:\\Book1.csv"
rows = [2,3,4]
columns = ['First Name', 'Age ', 'Sex']

query_csv(file,rows,columns)