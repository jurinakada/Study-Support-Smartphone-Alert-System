import gspread
from datetime import datetime


class GoogleSheetsReport:
    def __init__(
        self,
        report_content,
        json_keyfile="credentials.json",
        spreadsheet_name="FinalReport"
    ):
        # Scope settings
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        # Authenticate with the OAuth credentials.json
        client = gspread.oauth(
            credentials_filename=json_keyfile,
            authorized_user_filename="token_sheets.json",
            scopes=scope
        )

        # Open spreadsheet
        spreadsheet = client.open(spreadsheet_name)

        # Get the first worksheet
        worksheet = spreadsheet.sheet1

        # Save report content
        self.report_content = report_content
        self.worksheet = worksheet


    def send_report(self):
        try:
            # Get all values from the Google Spreadsheet
            all_values = self.worksheet.get_all_values()

            print("Current spreadsheet values:")
            print(all_values)

            # Header of the spreadsheet
            header = [
                "Date and Time",
                "Study Time",
                "Away Time",
                "Actual Study Time",
                "Phone Usage Time",
                "Warning Count",
                "Light Value",
                "Brightness",
                "Temperature",
                "Humidity"
            ]

            # If the spreadsheet is empty, add the header
            if len(all_values) == 0:
                self.worksheet.append_row(
                    header,
                    value_input_option="USER_ENTERED"
                )

            # If the existing header is different, replace it
            elif all_values[0] != header:
                print("Warning: The existing header is different!")

                self.worksheet.update(
                    range_name="A1:J1",
                    values=[header]
                )

            # Current date and time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Make the report list
            # self.report_content is already a list,
            # so combine it with current_time
            report_list = [
                current_time
            ] + self.report_content

            print("Report list:")
            print(report_list)

            # Check the number of values
            if len(report_list) != len(header):
                print("Error: The number of report values is incorrect.")
                print("Header columns:", len(header))
                print("Report columns:", len(report_list))
                return False

            # Add the report to a new row
            self.worksheet.append_row(
                report_list,
                value_input_option="USER_ENTERED"
            )

            print("Report was successfully added.")
            print(report_list)

            return True

        except Exception as error:
            print("Google Sheets Error:", error)
            return False


if __name__ == "__main__":
    # Test data
    test_report = [
        "00:60:00",
        "00:05:00",
        "00:55:00",
        "00:02:00",
        2,
        0.89,
        "Bright",
        25.0,
        50.0
    ]

    report = GoogleSheetsReport(test_report)

    report.send_report()