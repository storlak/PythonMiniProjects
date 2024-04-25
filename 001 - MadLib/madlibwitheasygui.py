import easygui as easy

yourname = ["What is your name: "]
country = ["Where are you from?: "]
city = ["Where do you live?: "]
age = ["How old are you?: "]
mariagestatus = ["What is your marriage status?: "]

for x in range(len(yourname)):
    question1 = easy.enterbox(yourname[x], "Madlib")
    question2 = easy.enterbox(country[x], "Madlib")
    question3 = easy.enterbox(city[x], "Madlib")
    question4 = easy.enterbox(age[x], "Madlib")
    question5 = easy.enterbox(mariagestatus[x], "Madlib")


print(
    f"Hello! My name is {question1}. I am from {question2} and I live in {question3}. I am {question4} years old and {question5}."
)
