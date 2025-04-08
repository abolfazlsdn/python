def should_serve_customer(customer_age, on_break, time):
    return customer_age>=21  and 5<time<10

print(should_serve_customer(20,True,7))