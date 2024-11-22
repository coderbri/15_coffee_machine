# 15 Coffee Machine

This project simulates the operation of a coffee vending machine that offers three types of beverages: **espresso**, **latte**, and **cappuccino**. Users can check available resources, make payments, and receive freshly brewed coffee. Designed as part of **Day 15** of the "100 Days of Code: Python Pro Bootcamp" by Dr. Angela Yu, the Coffee Machine project demonstrates key programming principles such as modular functions, input validation, and logical resource management.  


## Table of Contents
- [Features](#features)
- [Project Logic](#project-logic)
- [Example Walkthrough](#example-walkthrough)
- [How to Run](#how-to-run)


## Features

- **Menu Display**: Users can view the available drinks and their prices.  
- **Resource Report**: Shows the remaining water, milk, coffee, and earnings.  
- **Resource Validation**: Ensures the machine has enough resources to brew the selected coffee.  
- **Payment Handling**: Accepts coins (quarters, dimes, nickels, and pennies) and calculates total payment.  
- **Transaction Verification**: Processes payment and gives change if necessary.  
- **Beverage Preparation**: Deducts resources used and provides the selected drink.  
- **User-Friendly Exit**: Turn off the machine using the "off" command.  


## Project Logic  

1. **Menu Options**  
   - `menu`: Displays the available drinks along with their costs.  
   - `report`: Displays remaining resources and total earnings.  

2. **Input Validation**  
   - Prompts users to choose one of the listed drinks or check the menu/report.  
   - Handles invalid inputs gracefully with an error message.  

3. **Resource Management**  
   - Each drink requires specific amounts of water, milk, and coffee.  
   - Validates resource availability before proceeding.  

4. **Payment System**  
   - Accepts coins and calculates the total inserted.  
   - Verifies if the payment meets the drink's cost.  
   - Returns change if payment exceeds the cost or refunds if insufficient.  

5. **Coffee Preparation**  
   - Deducts required resources from the machine's inventory.  
   - Serves the selected coffee with a success message.  



## Example Walkthrough  

1. **Start the machine**  
   User is prompted:  
   ```
   What would you like (espresso/latte/cappuccino)?: latte  
   ```  

2. **Resource Check**  
   Machine checks if sufficient water, milk, and coffee are available.  

3. **Payment Processing**  
   User is prompted to insert coins:  
   ```
   Please insert coins.  
   > How many quarters?: 10  
   > How many dimes?: 0  
   > How many nickels?: 0  
   > How many pennies?: 0  
   Here is $2.50 in change.  
   ```  

4. **Drink Preparation**  
   ```
   Here is your latte ☕️  
   ```  

5. **Reporting**  
   ```
   What would you like (espresso/latte/cappuccino)?: report  
   +---------------+  
   |   RESOURCES   |  
   +---------------+  
   | Water    100ml |  
   | Milk      50ml |  
   | Coffee    76g  |  
   | Money   $2.50  |  
   +---------------+  
   ```


## How to Run  

1. Clone the repository.  
2. Ensure the `menu_resources.py` file and `main.py` file are in the same directory.  
3. Run `main.py` to start the Coffee Machine program.  


---
<section align="center">
  <code>coderBri © 2024</code>
</section>
