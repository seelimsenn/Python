import random

# result = dir(random)
# result = help(random)

result = random.random()
result = random.random() * 100
result = int(random.uniform(10, 100))
result = random.randint(1,100)

greeting = "Hello there!"
names = ['Ali', 'Veli', 'Ayşe', 'Fatma', 'Ahmet', 'Mehmet', 'Zeynep', 'Elif']
# result = names[random.randint(0, len(names)-1)]

result = random.choice(names)
result = random.choices(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste, 3)
# result = random.sample(names, 2)

print(result)