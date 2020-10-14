import datetime
print ("This is Anusheel's Personal Record Keeping Journal") 
char = str(input("Press J for Journal Keeping or B for Bank-Record Keeping: "))
journal = "j" or "J"
banking = "b" or "B"
x = datetime.datetime.now()
year = x.year
month = x.strftime("%b")
day_of_month = x.strftime("%d")
weekday = x.strftime("%A")


if char == journal:
    print(f"Journal for {year} - {month}{day_of_month} - {weekday}")
    journal_input = input ("Enter the date")

elif char == banking:
    print("Expense")

else:
    print("Invalid Character")
