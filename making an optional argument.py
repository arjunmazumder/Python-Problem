# making a argumant optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name} "
    else:
        full_name = f"{first_name} {last_name} "
    return full_name.title()
musician = get_formatted_name('arjun','mazumder')
print(musician)
musician = get_formatted_name('sanjida','riya','akter')    
print(musician)