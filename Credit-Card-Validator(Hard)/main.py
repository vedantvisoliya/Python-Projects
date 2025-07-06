# 378282246310005

number = "378282246310005"
numbers = "1234567890123456"

# 

def removeUnwantedChars(credit_card_number):
    new_credit_card_number = ""
    for num in credit_card_number:
        if num == " " or num == "-":
            new_credit_card_number += ""
        else:
            new_credit_card_number += num

    return new_credit_card_number


def enterCreditCardNumber():
    number = input("Enter your credit card number: ")
    credit_card_number = removeUnwantedChars(number)
    sum_of_digits_on_odd_places = 0
    sum_of_digits_on_even_places = 0
    sum = 0

    # sum digits from right to left on odd places
    for x in credit_card_number[::2]:
        sum_of_digits_on_odd_places += int(x)

    # sum of double of digits from right to left on even places 
    for x in credit_card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_of_digits_on_even_places += (1 + (x%10))
        else:
            sum_of_digits_on_even_places += x

    print(sum_of_digits_on_odd_places)
    print(sum_of_digits_on_even_places)
    
    # add both the sumissions
    sum = sum_of_digits_on_odd_places + sum_of_digits_on_even_places

    if (sum % 10 == 0): 
        print("Credit Card is Valid")
    else:
        print("Credit Card is Invlaid")
    
enterCreditCardNumber()