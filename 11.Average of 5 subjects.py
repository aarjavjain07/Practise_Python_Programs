#Python program to find out average marks of all the five subjects.

sub01 = float(input("Enter marks of subject 1 :"))
sub02 = float(input("Enter marks of subject 2 :"))
sub03 = float(input("Enter marks of subject 3 :"))
sub04 = float(input("Enter marks of subject 4 :"))
sub05 = float(input("Enter marks of subject 5 :"))
average = ( sub01 + sub02 + sub03 + sub04 + sub05 ) / 5
print("average marks of all the subject is :", format(average,".2f"))