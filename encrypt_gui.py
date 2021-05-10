from tkinter import *
from cryptography.fernet import Fernet

class Window:       
    def __init__(self, master):     
        self.filename=""
        csvfile=Label(root, text="File").grid(row=1, column=0)
        bar=Entry(master).grid(row=1, column=1) 

        

        #Buttons  
        y=7
        self.ebutton= Button(root, text="Encrypt", command=self.encrypt)
        y+=1
        self.dbutton= Button(root, text="Decrypt", command=self.decrypt)
        self.dbutton.grid(row=10, column=3, sticky = W + E)
        y+=1
        self.ebutton.grid(row=9, column=3, sticky = W + E)
        self.bbutton= Button(root, text="Choose File", command=self.browsecsv)
        self.bbutton.grid(row=1, column=3)

    def browsecsv(self):
        from tkinter.filedialog import askopenfilename
        Tk().withdraw() 
        self.filename = askopenfilename()

    def encrypt(self):
        if self.filename:

            key="w88I9dE0BAeugxLBD3UE2x8w4QeJBmmJJVgNNCwF49k="    

            fernet=Fernet(key)

            with open(self.filename,'rb') as file:
                original=file.read()

            encrypted = fernet.encrypt(original)

            with open(self.filename,'wb') as encrypted_file:
                encrypted_file.write(encrypted)


    def decrypt(self):
     
        key="w88I9dE0BAeugxLBD3UE2x8w4QeJBmmJJVgNNCwF49k="    

        fernet=Fernet(key)
        
        with open(self.filename,'rb') as enc_file:
            encrypted=enc_file.read()

        decrypted = fernet.decrypt(encrypted)    

        with open(self.filename,'wb') as dec_file:
            dec_file.write(decrypted)             


root = Tk()
window=Window(root)
root.mainloop()  