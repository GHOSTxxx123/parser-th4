import gspread
from google.oauth2.service_account import Credentials

def write_to_sheet(rows):
    scope = [
        'https://www.googleapis.com/auth/spreadsheets', 
        'https://www.googleapis.com/auth/drive'
    ]
    creds = Credentials.from_service_account_file(
        "google-credentials.json", scopes=scope,
        )
    client = gspread.authorize(creds)

    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1JmRMMqGWyCBi27lea-P2Z1FWRPdMHbfdqMyJFKUYGqM/edit?usp=sharing")
    worksheet = sheet.sheet1

    worksheet.append_rows(rows, value_input_option="RAW")

    