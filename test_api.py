import requests
import gspread
from google.oauth2.service_account import Credentials

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

CREDS_FILE = "credentials.json"
SHEET_NAME = "automation-lab-sheet"

def main():
    creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    
    sheet = client.open_by_key("1h8VN9n4Jhc4AEd-vi_ce7ECBCpcico7Vz5kn57dPsEU").sheet1
    sheet.clear()
    #sheet.update(range_name ="A1", values = [["Hello from Python"]])

    #sheet.update(range_name ="A2", values = [["Minh is building a home lab"]])
    #sheet.update(range_name="A1:C1", values=[["Asset Tag", "Status", "Owner"]])
    
    #sheet.append_row(["Laptop-01", "Assigned", "Minh"])
    #sheet.append_row(["Laptop-02", "In Stock", "Lan"])
    sheet.append_row(["ID","Title"])

    #records = sheet.get_all_records()
    #all_values = sheet.get_all_values()
    #for row in all_values:
    #    print(row)
    count = 0
    for post in data:
        if "title" in post and "sunt" in post["title"]:
            count += 1
            sheet.append_row([post["id"], post["title"]])

        if count >= 5:
            break
    print("Done. Google Sheets connection successful.")
if __name__ == "__main__":
    main()