import random

# Here we have three different statements that when put together will form your fortune for your zodiac that you
# put in.
currentSituation = ['You are stressed from all the impurities of life ',
                    'There does not seem to be a way out from where you are in life '
    , 'You seem to lack a sense of direction ', 'There is something that has been bugging you ']
positiveReinforcement = ['But there is always someone there for you in the end ',
                         'But you will not fail in what you do ',
                         'but you will always be able to rebound and look for the best in yourself ',
                         'but you will succeed in something that you have been doing ']
resolution = ['tomorrow, you will look brand new.', 'today will be the day you will finally get that big break.',
              'the future looks bright for your career.',
              'you will finally be able to rest.']

print("1 — Aries")
print("2 — Taurus")
print("3 — Gemini")
print("4 — Cancer")
print("5 — Leo")
print("6 — Virgo")
print("7 — Libra")
print("8 — Scorpio")
print("9 — Sagittarius")
print("10 — Capricorn")
print("11 — Aquarius")
print("12 — Pisces")
sign = int(input('Please enter your number for your Horoscope'))

# Here it prints the three statements together if the if statement is met.
if 0 < sign < 13:
    print(random.choice(currentSituation), random.choice(positiveReinforcement), random.choice(resolution))
else:
    print("Please enter a number between 0 and 12.")






