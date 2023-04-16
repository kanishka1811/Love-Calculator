print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_string = name1 + name2
x = combined_string.lower()

t = x.count("t")
r = x.count("r")
u = x.count("u")
e = x.count("e")

true = t + r + u + e

l = x.count("l")
o = x.count("o")
v = x.count("v")
e = x.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print (f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

# name1.lower()
# name2.lower()
#
# count1=0
# count2=0
#
# count1 += name1.count("t") + name2.count("t")
# count1 += name1.count("r") + name2.count("r")
# count1 += name1.count("u") + name2.count("u")
# count1 += name1.count("e") + name2.count("e")
#
# count2+= name1.count("l")+ name2.count("l")
# count2+= name1.count("o")+ name2.count("o")
# count2+= name1.count("v")+ name2.count("v")
# count2+= name1.count("e")+ name2.count("e")
#
# love_score= count1 +count2
#
# if love_score< 10 or love_score>90:
#     print (f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score> 40 and love_score<50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")
#












