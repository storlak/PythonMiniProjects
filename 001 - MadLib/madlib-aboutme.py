# madlib aboutme

while True:
    yourname = input("What is your name: ").capitalize()
    country = input("Where are you from?: ").capitalize()
    city = input("Where do you live?: ").capitalize()
    age = input("How old are you?: ")
    mariagestatus = input("What is your marriage status?: ")
    if (
        yourname.isdigit()
        or country.isdigit()
        or city.isdigit()
        or not age.isdigit()
        or mariagestatus.isdigit()
    ):
        print("Enter valid value")
    else:
        age = int(age)
        break

madlib = f"Hello! My name is {yourname}. I am from {country} and I live in {city}."
madlibe2 = f"I am {age} years old and {mariagestatus}."
print(madlib)
print(madlibe2)
