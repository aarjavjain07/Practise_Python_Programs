date = int(input("Enter today's date :"))
month = int(input("Enter month number : "))
list_date = [31,28,31,30,31,30,31,31,30,31,30,31]
list_month = ["January", "February", "March", "Arpil", "May", "June", "July", "August", 
              "September", "October", "November", "December"]
print("\nYou are in", list_month[month - 1], "and it has total",list_date[date - 1],"days and"
      ,list_date[date - 1] - date, "days are left in this month.")