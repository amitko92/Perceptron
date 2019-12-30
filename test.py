from Perceptron import Perceptron
from openpyxl import Workbook
import random as rand
import datetime
wb = Workbook()

# grab the active worksheet
ws = wb.active

train_group = []
train_group_data = []
x = 0
y = 0
type = 0

for i in range(100):
    x = rand.randint(-50, 50)
    y = rand.randint(-50, 50)

    if y < 0:
        type = 0
    else:
        type = 1

    train_group.append([x, y])
    train_group_data.append(type)
    ws.append([x, y, type])

# Save the file
wb.save("train_group.xlsx")

print(train_group_data)
print(train_group)

wb = Workbook()

# grab the active worksheet
ws = wb.active

test_group = []
test_group_data = []
number_of_0 = 0
number_of_1 = 0
x = 0
y = 0
type = 0

for i in range(100):
    x = rand.randint(-50, 50)
    y = rand.randint(-50, 50)

    if y < 0:
        type = 0
        number_of_0 += 1
    else:
        type = 1
        number_of_1 += 1

    test_group.append([x, y])
    test_group_data.append(type)
    ws.append([x, y, type])

wb.save("test_group.xlsx")

p = Perceptron(2, 0)
p.training(train_group, train_group_data)
count_true_pra = 0
count_false_pra = 0

for instance, type in zip(test_group, test_group_data):
    temp = p.val(instance)
    if temp == type:
        if type == 0:
            count_true_pra += 1
        else:
            count_false_pra += 1
    else:
        print("False:" + str(instance) + " type: " + str(type))
        print("Temp: " + str(temp))

print("count true detection: " + str((count_true_pra/number_of_0)))
print("count true detection: " + str((count_false_pra/number_of_1)))

