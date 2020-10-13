print ("This is Anusheel's Personal Record Keeping Journal") 
char = str(input("Press J for Journal Keeping or B for Bank-Record Keeping: "))

if char == "J" or "j":
    j_user = input("What Motivated you Today?: ")
    j_user_a = input ("How many minutes did you meditate?: ")
    j_user_b = input("WHat made you feel stressed?: ")

elif char == "B" or "b":
    count_inflow = input("How many times did cash inflow occured? ")
    for i in count_inflow:
        b_user_inflow = input(f"Cash Inflow for {day}: ")
        b_user_remarks_in = input(f"Remarks for Cash Inflow: ")
    count_outflow = input("How many times did cash inflow occured? ")
    for i in count_outflow:
         b_user_inflow = input(f"Cash Outflowflow for {day}: ")
         b_user_remarks_out = input(f"Remarks for Cash Outflow: ")
else:
    print("Error Invalid Character")