# Detects potential fraudsters (customers who pay less than 30% tax rate)

customers = ["James", "John", "Robert", "Mary", "Patricia", "Jennifer"]
salary = [155000, 755000, 455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]


def find_fraud(c_list, s_list, t_list):
    potential_fraud = []

    for i in range(len(c_list)):
        if t_list[i] / s_list[i] < 0.3:
            potential_fraud.append(c_list[i])
    
    return potential_fraud


fraudsters = find_fraud(customers, salary, taxes)
print(fraudsters)