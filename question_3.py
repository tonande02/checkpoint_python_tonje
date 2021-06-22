# A program that scores salesmen based on performance

jordan_belfort = {"calls": 178, "meetings": 17, "sales": 6}

def sales_score(s_dict):
    score = 0
    
    score += s_dict["calls"] * 10
    score += s_dict["meetings"] * 30
    score += s_dict["sales"] * 100

    if  s_dict["calls"] > 150:
        score += 100
    
    if  s_dict["meetings"] > 20:
        score += 100
    
    if  s_dict["sales"] > 5:
        score += 100

    s_dict["score"] = score

    return s_dict


barry_allen = {"calls": 150, "meetings": 25, "sales": 4}
diana_prince = {"calls": 160, "meetings": 22, "sales": 7}

j_b_score = sales_score(jordan_belfort)
b_a_score = sales_score(barry_allen)
d_p_score = sales_score(diana_prince)

print(f"J. Belfort: {j_b_score}")
print(f"B. Allen: {b_a_score}")
print(f"D. Prince: {d_p_score}")