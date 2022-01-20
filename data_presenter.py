# get all
open_file = open("CupcakeInvoices.csv")
for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values)

# get the type of cupcake
open_file.seek(0)
for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values[2])

# get individual totals
open_file.seek(0)
for line in open_file:
    line = line.strip()
    values = line.split(",")
    print( int(values[3]) * float(values[4]))

numbers = []

# get total overall
open_file.seek(0)
for line in open_file:
    line = line.strip()
    values = line.split(",")
    numbers.append(int(values[3]) * float(values[4]))
total = sum(numbers)
print(total)

# close file
open_file.close()