import math

# Validate customer code

def check_cust_code(code):
    valid_code = {'R', 'C', 'I'}
    return code.upper() in valid_code

# User input code

cust_code = input('Enter customer code (R, C, or I): ')

if not check_cust_code(cust_code):
    print('Invalid input (customer code)')

# User input readings

else:   
    start_read = int(input('Enter beginning reading (between 0 and 999999999): '))
    end_read = int(input('Enter ending reading (between 0 and 999999999): '))

    # Validate value
    
    if not (0 <= start_read <= 999999999) or not (0 <= end_read <= 999999999):
        print('Invalid input (beginning or ending reading value is out of range)')

    else:

        gal = end_read - start_read + 1000000000 if end_read < start_read else end_read - start_read
        gal_used = gal / 10

        # CODE R
        
        if cust_code == 'R':
            bill = 5.00 + gal_used * 0.0005

        # CODE C
        
        elif cust_code == 'C':
            if gal_used <= 4000000:
                bill = 1000.00
    
            else:
                bill = 1000.00 + (gal_used - 4000000) * 0.00025

        # CODE I
            
        elif cust_code == 'I':
            if gal_used <= 4000000:
                bill = 1000.00
            
            elif gal_used <= 10000000:
                bill = 2000.00
            
            else:
                bill = 2000.00 + (gal_used - 10000000) * 0.00025

        #make reading values always 9 digits
        
        start_read_str = f'{start_read:09}'
        end_read_str = f'{end_read:09}' 

        print(f'Customer code: {cust_code}')
        print('Beginning reading value in gallons and tenths of gallon:', start_read_str)
        print('Ending reading value in gallons and tenths of gallon:', end_read_str)
        print(f'Gallons of water used: {gal_used:0.1f}')
        print(f'Amount billed: ${bill:0.2f}')