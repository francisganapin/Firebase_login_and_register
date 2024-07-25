import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QApplication
from PyQt6.QtCore import QTimer
from datetime import datetime
import pyrebase

from PyQt6 import QtCore, QtWidgets




class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        try:
            # Load the UI file
            uic.loadUi('main.ui', self)

            # Set fixed size based on loaded UI
            self.setFixedSize(self.size())

            ##if you have problem on databaseUrl just copy the authDomain
            #then add http://the the auto domain

            self.firebaseConfig = {
            'apiKey': "AIzaSyDzSwdg9QKjSYsj2xpl_6Rpeo6qthJ6T34",
            'authDomain': "projectshow-73dac.firebaseapp.com",
            'databaseURL':'http://projectshow-73dac.firebaseapp.com',
            'projectId': "projectshow-73dac",
            'storageBucket': "projectshow-73dac.appspot.com",
            'messagingSenderId': "378019437434",
            'appId': "1:378019437434:web:6208744995beac907114c3",
            'measurementId': "G-9XC58HSN6Y"
            }

            self.firebase = pyrebase.initialize_app(self.firebaseConfig)
            self.db=self.firebase.database()
            self.auth=self.firebase.auth()
     
            self.save_bt.clicked.connect(self.login_auth)
            self.register_bt.clicked.connect(self.register_account)

        except FileNotFoundError:
            print("UI file 'main2.ui' not found.")


    def login_auth(self):
        #authentication
        #Login
        self.email = self.email_input.text()
        self.password = self.password_input.text()
        try:
            self.auth.sign_in_with_email_and_password(self.email,self.password)
            print('connected')
            self.label_page_1.setText(f'connected')
        except:
            print('not connected')
            self.label_page_1.setText(f'not connected invalid password or email')


    def register_account(self):
        #register account
        #register

        #signup
        #register sections 
        register_email = self.email_input_2.text()
        register_password = self.password = self.password_input_2.text()
        register_confirm_password = self.password = self.password_input_3.text()

        if register_password==register_confirm_password:
            try:
                self.auth.create_user_with_email_and_password(register_email,register_confirm_password)
                self.label_page_2.setText(f'email created with name of {register_email}')
            except Exception:
                self.label_page_2.setText(f'email was already in use {register_email}')
        else:
            self.label_page_2.setText(f'Password and Confirm was not same')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MyApp()
    main_app.show()
    sys.exit(app.exec())


import pyrebase





#For those who have error you encounter 
#no  'databaseURL  if give you solution to your problem since i already encounter 

#self.firebaseConfig = {
#            'apiKey': "AIzaSyqwe123szSYsj2xpl_6Rpeozxczxczx6qthJ6T34",
#            'authDomain': "example-714dac.firebaseapp.com",
#            'databaseURL':'http://example-714dac.firebaseapp.com',
#            'projectId': "example-714dac",
#            'storageBucket': "example-714dac.appspot.com",
#            'messagingSenderId': "378019437434",
#            'appId': "1:3713221312437434:web:6312395beaczxczc907114c3",
#            'measurementId': "G-312316Y"
#            }

#You just need to copy the 'authDomain': "example-714dac.firebaseapp.com", <--- this one 
#then add http://example-714dac.firebaseapp.com it should be run 
