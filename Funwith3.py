def display_info(**kwargs):
    for key, value in kwargs.item():
       print(f"{key}: {value}")

display_info(name="alice" , age=30, city="new york")