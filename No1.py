path = r"C:\Users\HP Core i5\Documents\python\Task III"

def sum_of_numbers_from_file(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            total += int(line.strip())
    return total

filename = path + '\\indata.txt'
result = sum_of_numbers_from_file(filename)
print("{:,.2f}".format(result))
