import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

class GoogleSheetsReport:
    def__init__(self, json_keyfile="credentials.json", spreadsheet_name="FinalReport"):
       #scope settings
        scope = [
        https://www.googleapis.com/auth/spreadsheets,
        https://www.googleapis.com/auth/drive]
    #load the credential information
    credentials = Credentials.from_service_account_file(
        'credentials.json',
        scopes=scope

    )
    report_list = []
    #initalize client
    client = gspread.authorize(credentials)\
    
    #open spread sheet or make new one
    spreadsheet = client.open("final_report")

    #get the all values on the google spread sheet
    all_values = worksheet.get_all_values()
    
    #renew and input the final report data
    worksheet,update('',report_list)


