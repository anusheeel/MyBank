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
    journal_entry_1 = str(input("New things learned: "))
    journal_entry_2 = input("how many minutes meditated? ")
    journal_entry_3 = input("how many minutes workout? ")
    journal_entry_4 = str(input("Anything distracting? "))
    
elif char == banking:
    print(f"Expense record for {year} - {month}{day_of_month} - {weekday}")
    tod = ['morning', 'afternoon' , 'evening']
    for i in tod:
        banking_counter = int(input(f"How many times expense occured in {i}? "))
        for j in range(banking_counter):  
            banking_entry = input(f"Expense in the {i} _ {j}: ")
            banking_entry_1 = str(input(f"Remarks for the {i} _ {j}: "))
        

else:
    print("Invalid Character")
