import csv
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from creds.items import Items
from creds import credentials


class SendMonthsReport:

    @staticmethod
    def send_month(month):
        today = date.today()
        d4 = today.strftime("%Y")

        send_month = month + d4

        try:
            file_object = open(Items.FILE_REPORT_PATH % send_month, 'r')
            lines = csv.reader(file_object, delimiter=',', quotechar='"')
            flag = 0
            data = []
            for line in lines:
                if line == []:
                    flag = 1
                    continue
                else:
                    data.append(line)
            file_object.close()
            if flag == 1:  # if blank line is present in file
                file_object = open(Items.FILE_REPORT_PATH % send_month, 'w')
                for line in data:
                    str1 = ','.join(line)
                    file_object.write(str1 + "\n")
                file_object.close()
        except Exception as e:
            print (e)

        with open(Items.FILE_REPORT_PATH % send_month) as csvfile:
            row_count = sum(1 for row in csvfile)
            print(row_count)



        with open(Items.FILE_REPORT_PATH % send_month, 'r') as csv_file:
            reader = csv.reader(csv_file)

            dates_list = []

            for row in reader:
                if len(row) == 0:
                    continue
                dates_list.append(row)
            dates_list.sort(reverse=False)

            row_count_two = (str(dates_list).replace("[", "").replace("]", "").replace("'", ""))
            print(row_count_two)

        working_days = row_count
        working_time = row_count * 9

        # storing the senders email address

        sender = credentials.DOCUMENT_SENDER_EMAIL
        send_to_email = [Items.EMAIL_DMITRIY]

        password = credentials.DOCUMENT_SENDER_EMAIL_PASSWORD

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender, password)

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ", ".join(send_to_email)
        msg['Subject'] = 'Risukhin Dmitriy Work From Home'

        file = Items.FILE_REPORT_PATH % send_month

        text1 = "Hello. My working days and hours in month %s" % send_month + "\n"

        text2 = "My dates: " + row_count_two + "\n"

        text3 = "Days: " + str(working_days) + "\n" + \
                "Total hours: " + str(working_time) + "\n"

        part1 = MIMEText(text1, 'plain')
        part2 = MIMEText(text2, 'plain')
        part3 = MIMEText(text3, 'plain')
        msg.attach(part1)
        msg.attach(part2)
        msg.attach(part3)

        # open and read the CSV file in binary
        with open(file, 'rb') as file:
            # Attach the file with filename to the email
            msg.attach(MIMEApplication(file.read(), Name="%s.csv" % send_month))

        server.sendmail(sender, send_to_email, msg.as_string())

