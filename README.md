# Password-Locker
This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.
# Author 
Joan Kirui [joankirui99@gmail.com]
# User Stories
The user would like to.... :
  * To create an account for the application or log into the application.
  * Store my existing acounts login details for various accounts that i have registered for.
  * Generate new password for an account that i haven't registered for and store it with the account name.
  * Delete stored account login details that i do now want anymore.
  * Copy my credentials to the clipboard
# Installation / Setup instruction
## The application requires the following installations to operate
  * python3.6
  * pyperclip
  * pip
## Cloning
  * Open Terminal {Ctrl+Alt+T}
  * git clone https://github.com/joankirui/Password-Locker.git
  * cd Password-Locker
  * code . or atom . based on the text editor you have.
# Running the Application
  * To run the application, open the cloned file in terminal and run the following commands: 
    * $ chmod +x run.py
    * $ ./run.py
  * To run test for the application $ python3 passlock_test.py
# Behaviour Driven Development
 | Behaviour | Input | Output |
 |-----------|--------|-------|
 |Open the application on the terminal| Run the command $ ./run.py | Hello welcome to your credentials store *ca-create new account *ha-have an account|
 |Select ca|input username and password | Hello username, Your account has been created succesfully! Your password is: password|
 |Select ha|Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
 |Store a new credential in the application|Enter cc|Enter Account, username, password choose ip to enter your password or gp for the application to generate a password for you |
 |Display all stored credentials|Enter dc|A list of all credentials that has been stored or You don't have any credentials saved yet|
 |Find a stored credential based on account name|Enter fc|Enter the Account Name you want to search for and returns the account details|
 |Delete an existing credential that you don't want anymore|Enter d|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exists|
 |Exit the application|Enter ex|The application exits|
 

# Technologies Used
  * python3.6
# License
  * MIT License:
  * Copyright (c) 2021 Joan Kirui

