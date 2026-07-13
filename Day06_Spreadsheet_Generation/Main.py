#Importing Necessary Libraries
import openpyxl

currency_list = ["USD", "EUR", "GBP", "JPY", "AUD", "INR"]
with open("system_logs.txt", "r") as file:
    line_count = sum(1 for line in file)
    print("Total number of lines in the file:", line_count)
    file.close()
#Reading the system_logs.txt
with open("system_logs.txt", "r") as file:
    for i in range(line_count+1):
        logs = file.readline()
        if "USER_EXPENSE" in logs:
            list = logs.split(" INFO - ")
            date = list[0].split()[0]
            time = list[0].split()[1]
            info = list[1].split(":",1)
            info.append(info[1].split("|"))
            info.append(info[2][2].split())
            category = info[2][0]
            details = info[2][1]
            price = info[3][0]
            currency = info[3][1]
            print("Date:", date)
            # print("Time:", time)
            # print("Category:", category)
            # print("Details:", details)
            # print("Price:", price)
            print("Currency:", currency)

        else:
            print("Ignoring the INVALID_FORMAT_LINE")