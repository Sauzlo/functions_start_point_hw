def return_10():
    return 10

def add(num_1, num_2):
    total = num_1 + num_2
    return total

def subtract(num_1, num_2):
    total = num_1 - num_2
    return total

def multiply(num_1, num_2):
    total = num_1 * num_2
    return total

def divide(num_1, num_2):
    total = num_1 / num_2
    return total

def length_of_string(string):
    length = len(string)
    return length

def join_string(string_1, string_2):
    strings = string_1 + string_2
    return strings

def add_string_as_number(string_1, string_2):
    total = int(string_1) + int(string_2)
    return total

def number_to_full_month_name(num):
    months = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
    selected = months[num - 1]
    return selected

def number_to_short_month_name(num):
    months = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
    selected = months[num - 1]
    return selected[:3]

def calculate_volume_from_side(num):
    volume = num ** 3
    return volume

def reverse_current_string(string):
    gnirts = string[::-1]
    return gnirts

def convert_f_to_c(fahrenheit):
    celcius = ((fahrenheit - 32) * 5) / 9
    return celcius