## Project Name

Password Locker

## Author

UMUTESIWASE Yvette

## Description

Password Locker is a terminal run python application that allows users to store details example: usernames and passwords of their various accounts

## User Stories

* As a user, I want to create a password locker account with my details, a login username and password.

* As a user, I want to store my already existing account credentials in the application. Assuming I already have a twitter account, I want to store my already existing twitter username and password in the application.

* As a user, I want to create new account credentials in the application. For example, if I have not yet signed up for Instagram, I would want to create a credentials account for Instagram in the application and the application generates a password for me to use when I sign up for Instagram.

* As a user, I want to have the option of putting in a password that I want to use for the new credential account. For example, when creating my Instagram credential account, I want to have an option of putting in the password I want to use instead of having the application generate a password for me.

* As a user, I also want to view my various account credentials and their passwords in the application.
* As a user, I want to delete a credentials account that I no longer need in the application.

## Specifications

|Behaviour                   |            Input            	|Output|
|Display codes for navigation|	In terminal: $./password_locker.py|	Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit|
Display prompt for creating an account	Enter: ca	Enter your first name, last name and password
Display prompt for login in	Enter: li	Enter your account name and password
Display codes for navigation	Successful login	Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit
Display prompt for creating a credential	Enter: cc	Enter the site name, your username and password
Display a list of credentials	Enter: dc	Prints a list of saved credentials
Display prompt for which credential to copy	Enter: copy	Enter the site name of the credential you wish to copy.
Exit application	Enter: ex	Exit the current navigation stage


## SetUp / Installation Requirements

* python3.6
* chmod +x run.py
* ./run.py
* run this command lines in your terminal: https://github.com/umutesiwaseyvette/Password-Locker

## Contact

* Tel:+250788582184
* Email: rwjpyy@gmail.com

## License

MIT License

Copyright (c) 2019 UMUTESIWASE Yvette
