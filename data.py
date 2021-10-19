from faker import Faker

fake = Faker()

count = 10000
data = []
for i in range(count):
    name = fake.name()
    temp = {
        'name': name,
        'login': name.split()[0],
        'password': fake.password(),
        'address': name.split()[0] + '@gmail.com'
    }
    data.append(temp)

print(len(data))