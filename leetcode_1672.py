def find_richest_customer(bank_collection):
    richest = 0
    for customer in bank_collection:
        richest = max(richest, sum(customer))
    return richest


print(find_richest_customer([[1,2,4], [2,4,5]]))