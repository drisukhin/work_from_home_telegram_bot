from datetime import date
from creds.items import Items

class CreateNewFileReport:

    @staticmethod
    def create_new_file_report():
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        d2 = today.strftime("%d")
        d3 = today.strftime("%B")
        d4 = today.strftime("%Y")

        if d2 == "01":
            with open(Items.FILE_REPORT_PATH % (d3 + d4), 'a', encoding="utf-8") as file:
                file.close()
