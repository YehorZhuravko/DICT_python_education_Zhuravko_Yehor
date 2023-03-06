import random

# Кількість друзів
num_friends = int(input("Enter the number of friends joining (including you): "))
while int(num_friends) <= 1:
        print("No one is joined for the party!")
        exit()

# Формування списку
friends = []
for i in range(num_friends):
    name = input("Enter friend #{}'s name: ".format(i+1))
    friends.append(name)

# Загальна сума грошей і роздрук списку друзів
total_money = float(input("Enter the total amount of money that your friends brought: "))
money_per_friend = total_money / num_friends
print("Your friends are:")
for friend in friends:
    print("- " + friend)

# Функція "Who is lucky?"
answer = input("Do you want to use the 'Who is lucky?' feature? (Yes/No): ")
if answer.lower() == "no":
    print("Each friend brought {:.2f} dollars.".format(money_per_friend))
else:
    lucky_friend = random.choice(friends)
    print("{} is the lucky one!".format(lucky_friend))

    # Обнулення грошей щасливого друга та поділ їх порівну між рештою друзів
    m_without_lucky = total_money / (num_friends - 1)
    print()
    for friend in friends:
        if friend != lucky_friend:
            print("{} gets {:.2f} dollars.".format(friend, m_without_lucky))
        else:
            print("{} gets nothing.".format(lucky_friend))
