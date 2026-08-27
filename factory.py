class StudentIDCard:
    def issue_card(self):
        print("student id issued")

class FacultyIDCard:
    def issue_card(self):
        print("faculty id issued")

class StaffIDCard:
    def issue_card(self):
        print("Staff id issued")

class IDCardFactory:

    def get_card(self,card_type):


        if card_type=="Student":
            return StudentIDCard()
    
        elif card_type == "Faculty":
            return FacultyIDCard()  
        
        elif card_type=="Staff":
            return StaffIDCard()
            
        else:
            print("invalid input")
            return None

factory = IDCardFactory()

card= factory.get_card("Student")
card.issue_card()

card= factory.get_card("Faculty")
card.issue_card()

card= factory.get_card("Staff")
card.issue_card()
