import csv
from datetime import date
from creds.items import Items

class CheckMonthsReport:
    @staticmethod
    def month(month):
        today = date.today()
        d4 = today.strftime("%Y")
        send_report = month + d4

        with open(Items.FILE_REPORT_PATH % send_report, 'r') as csv_file:
            reader = csv.reader(csv_file)

            dates_list = []

            for row in reader:
                if len(row) == 0:
                    continue
                dates_list.append(row)
            dates_list.sort(reverse=False)

            row_count_two = (str(dates_list).replace("[", "").replace("]", "").replace("'", ""))
        return row_count_two
