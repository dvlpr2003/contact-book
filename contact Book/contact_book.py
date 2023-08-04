import os
class Contactbook():
    def __init__(self):
        self.Details = {}
    def Add_contact(self):
        add = True
        while add :
          name = input("Name: ")  
          Mobile_number = (input("Mobile Number: "))
          
          Address1 = input("Address line 1 : ").capitalize()
          Address2 = input("Address line 2 : ").capitalize()
          Pincode = (input('Pincode : '))
          Email = input("email: ")

          self.Details[name] = [Mobile_number,Address1,Address2,Pincode,Email]

          confirm = input("Do you want to add more contact details(y/n): ")
          if confirm == "y" or confirm == "Y":
              add = True
          elif confirm == "n" or confirm == "N":
              add = False
          else:
              print("Select valid option")
              break
    def Show_details(self):
        print("Contact lists")
        list1 = []
        number = 1
        for _ in self.Details:
            print(f"{number}.{_}")
            number+=1
            list1.append(_)

        select_contact = int(input("which contact you want to view: "))
        os.system("clear")

        print(f"         {list1[select_contact-1]}         ")
        print(f"Mobile Number: {self.Details[list1[select_contact-1]][0]}")
        print(f"Address line 1: {self.Details[list1[select_contact-1]][1]}")
        print(f"Address line 2: {self.Details[list1[select_contact-1]][2]}")
        print(f"Postal code : {self.Details[list1[select_contact-1]][3]}")
        print(f"Email: {self.Details[list1[select_contact-1]][4]}")

            


      


        


        