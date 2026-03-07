#!/usr/bin/python
#Tuple for the string used 
PLAN_TYPE_TUPLE = ("C", "c", "R", "r", "S", "s")


#STEP 1 and STEP 2: Get data from the user and proceed only after the user inputs correct data else print invalid 
# correct string within the plan_type_tuple , the correct minutes i.e cannot be negative number or max amount of minutes in a week 

def get_and_validate_talk_time():
    plan_type = input("Enter the plan type: C/c for Commercial, R/r for Residential, S/s for Student :")
    while plan_type.lower() not in PLAN_TYPE_TUPLE:
        plan_type = input("Invalid Input: Enter the plan type: C/c for Commercial, R/r for Residential, S/s for Student :")
 
    min_talked = float(input("Enter the minutes talked: "))
    while not 0 <= min_talked <= 10080:
        min_talked = float(input("Invalid Input: Enter the minutes talked between 0 and 10080: "))
 
    return plan_type.upper(), min_talked
 
#STEP 2 : Calcultes the talk_time and the total_ amount with out the pre_paid_payment 
#Commercial - 0.20 for first 300 , 0.10 for anything over 300
#Residential - 0.10 for every 120 ,0.05 per min for anything over 120
#Student - $0.15 per minutes
def calculate_talk_time(plan_type, talk_minutes):
    total_amount =0
    amount_remaining =0

    if plan_type in ("C", "c"):
        rate_per_minute = 0.20
        free_minutes = 300
        if talk_minutes <= free_minutes:
            amount = rate_per_minute * talk_minutes
        else:
            amount = rate_per_minute * free_minutes
            extra_minutes = talk_minutes - free_minutes
            amount_remaining = 0.10 * extra_minutes
 
    elif plan_type in ("R", "r"):
        rate_per_minute = 0.10
        free_minutes = 120
        if talk_minutes <= free_minutes:
            amount = rate_per_minute * talk_minutes
        else:
            amount = rate_per_minute * free_minutes
            extra_minutes = talk_minutes - free_minutes
            amount_remaining = 0.05 * extra_minutes
 
    elif plan_type in ("S", "s"):
        rate_per_minute = 0.15
        amount = rate_per_minute * talk_minutes
    else:
        return None  # Invalid plan type
 
    total_amount = amount + amount_remaining
    return total_amount
 
#Step3 : Calculates the total amount owed or total credit reamininig and prints out the result 


def main():
    customer_id = 0
    customer_info_list = []
    pre_paid_amount = 25

    while True:
        customer_id += 1
        plan_type, min_talked = get_and_validate_talk_time()
        total_amount = calculate_talk_time(plan_type, min_talked)
        print('----------------INVOICE----------------')
        print("Total Price: ${:.2f}".format(total_amount))
        if total_amount > pre_paid_amount:
            print("Amount Due: ${:.2f}".format(total_amount - pre_paid_amount))
        else:
            print("Remaining Credit: ${:.2f}".format(pre_paid_amount - total_amount))
    
        # Creates a dictionary 
        customer_info ={
            "ID": customer_id,
            "Minutes Used": min_talked,
            "Plan Type": plan_type,
            "Amount": total_amount
        }
        customer_info_list.append(customer_info)

        more_cust = input("Would you like to enter customer information yes/no?")
        if more_cust.lower() != "yes":
            break

        print("\nCustomer Data Table:")
        print("{:<15} {:25} {:<10} {:<15}".format("Customer ID", "Plan Type", "# minutes", "Amount"))
        print("-" * 65)

        for customer_dictionary in customer_info_list:
            cust_id = customer_dictionary["ID"]
            cust_plan_type = customer_dictionary["Plan Type"]
            cust_min_talked = customer_dictionary["Minutes Used"]
            cust_total_amount = customer_dictionary["Amount"]
            print("{:^13} {:^25} {:^10} {:^20.2f}".format(cust_id, cust_plan_type, cust_min_talked, cust_total_amount))

if __name__ == "__main__":
    main()

        

 