date = input("Enter today's date: ")
mood = input("Enter your mood, lying somewhere between 1 to 10: ")
journal_entry = input("Enter your thoughts\n")

with open(f"journal/{date}.txt",'w') as f:
    f.write("Today's Date: ")
    f.write(date)
    f.write("\nToday's general mood: ")
    f.write(mood)
    f.write("\nEntry:\n")
    f.write(journal_entry)