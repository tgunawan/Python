import os

directory = "./Jojo/KontakApp/Data/"
class ContactManager:
    def __init__(self,filename="contacts.txt"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        contacts = []
        if os.path.exists(self.filename):
            with open(directory+self.filename,'r') as f:
                for line in f:
                    name, phone = line.strip().split(",")
                    contacts.append((name,phone))
        return contacts
    
    def save_contacts(self):
         with open(directory+self.filename,'w') as f:
                for name, phone in self.contacts:
                    f.write(f"{name},{phone}\n")

    def add_contact(self,name,phone):  
        self.contacts.append((name,phone))
        self.save_contacts()

    def get_all_contact(self): 
        return self.contacts