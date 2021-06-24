# Detects potential fraudsters (customers who pay less than 30% tax rate)

# 1a (level 1)
# customers = ["James", "John", "Robert", "Mary", "Patricia", "Jennifer"]
# salary = [155000, 755000, 455000, 1255000, 635000, 575000]
# taxes = [55800, 317100, 182000, 451800, 171450, 71400]


# def find_fraud(c_list, s_list, t_list):
#     potential_fraud = []

#     for i in range(len(c_list)):
#         if s_list[i] > 555000 and t_list[i] / s_list[i] < 0.3:
#             potential_fraud.append(c_list[i])
    
#     return potential_fraud


# fraudsters = find_fraud(customers, salary, taxes)
# print(fraudsters)




# 1b (level 2)
# I arranged the data in a .csv file with name;salary;taxes as the columns
# (see 'customers.csv' in the repo)
# NB: not sure about the implementation of the try/except/finally - 
# if I've done it right

def fraud_from_file(filename):
    customer_file = ""

    try:
        customer_file = open(file=filename, mode='r')
        categories = customer_file.readline().split()
        potential_frauds = []

        for line in customer_file:
            line = line.split()

            name = line[0]
            salary = int(line[1])
            taxes = int(line[2])

            if salary > 555000 and taxes / salary < 0.3:
                potential_frauds.append(name.capitalize())
        
        return potential_frauds
    except FileNotFoundError:
        print("Error: File not found")
    finally:
        if customer_file:
            customer_file.close()


print("Customers with salary above 555000 and less than 30% tax rate:")
print(fraud_from_file("customers.csv"))