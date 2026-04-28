![My Banner](/images/ATM%20Banner.png)
# ATM Desktop Application
### Brief 
This project is a comprehensive ATM desktop application built using Tkinter for the graphical user interface and SQLite as the database backend. The application supports essential banking functionalities, including:

- Login and Sign Up with validation.
- Deposit and Withdraw funds.
- Donations to various charities and organizations.
- Check your Account Balance.
- Transfer Money between accounts.
- Currency Conversion to Egyptian Pounds (EGP).
- The application is user-friendly and designed to simulate real-world banking operations while being robust and secure.

### Tutorial
#### Running the Application:

1.Clone the repository to your local machine:
Copy code
```bash
git clone <repository-link>
```
2.Navigate to the project directory:
``` bash
cd ATM_Desktop_App
```
3.Install the required dependencies (see the Requirements section).

4.Launch the application by running:
```bash
python main.py
```
### Using the Application:
<b>1.Sign Up:</b>
- Create a new account by entering your details. Password validation ensures strong credentials.

<b>2.Login:</b>
- Access your account using your registered credentials.

<b>3.Deposit/Withdraw:</b>
- Deposit or withdraw amounts with instant updates to your account balance.

<b>4.Donations:</b>
- Make contributions to listed charities and organizations.

<b>5.Balance Check:</b>
- View your current account balance.

<b>6.Money Transfer:</b>
- Transfer funds securely between accounts.

<b>7.Currency Conversion:</b>
- Convert your balance to Egyptian Pounds (EGP).

## Requirements to Install the Application
To run the application, ensure the following are installed on your system:

<b>Python 3.8 or later: [Download Python](https://www.python.org/downloads/)</b>


```bash
pip install -r requirements.txt
```
### Entity-Relationship Diagram (ERD)
The ERD below represents the application's database structure:
![ERD](/images/image-1.png)

### Team Members
- Abdallah Beshary [contact](https://www.linkedin.com/in/abdallahbeshary/)
- Hana Nazmy [contact](https://www.linkedin.com/in/hana-nazmy-b065b925b/)
- Hana Gamal [contact](https://www.linkedin.com/in/hana-gamal-abuelyazeed/)
- Fatma Ahmed [contact](https://www.linkedin.com/in/fatma-ahmed-6487a6256/)
- Shahd Abdallah [contact](https://www.linkedin.com/in/shahd-abdallah-bb1753286/)
- Nada Ayman [contact](https://www.linkedin.com/in/nada-ayman-6296b5254/)




<!-- Functions
Key Functions in the Application:
User Registration (register_user):
Handles new user sign-ups with validation for strong passwords and unique usernames.
User Login (login_user):
Validates user credentials to grant access.
Deposit Funds (deposit_funds):
Adds the specified amount to the user's account balance.
Withdraw Funds (withdraw_funds):
Deducts the specified amount from the user's account balance, ensuring sufficient funds.
Donation (make_donation):
Processes donations and logs them in the database.
Balance Check (check_balance):
Retrieves and displays the current balance for the user.
Transfer Funds (transfer_funds):
Allows transferring money between two accounts.
Currency Conversion (convert_currency):
Converts the user's balance to Egyptian Pounds (EGP) based on the latest exchange rates.
Feel free to contribute, report issues, or suggest features to make this application even better! -->

<!-- 
## License

[MIT](https://choosealicense.com/licenses/mit/) -->
