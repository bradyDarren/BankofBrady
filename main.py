from customers import Customers

first_name = input("first_name: ")
last_name = input("last_name: ")
social = input("social: ")
phone = input("phone: ")
email = input("email: ")
citizen = input("citizen: ")

customer_info = Customers(f_name=first_name, l_name=last_name, 
                          ssn=social, phone_num=phone,email=email,us_cit=citizen)

print(customer_info.f_name, customer_info.l_name)

customer_info.name_change(change=True, new_name="Johnson")

print(customer_info.f_name,customer_info.l_name)