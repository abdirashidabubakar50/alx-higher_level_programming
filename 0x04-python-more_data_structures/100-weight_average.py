def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_of_products = 0
    sum_of_weights = 0
    for elements in my_list:
        value, weight = elements
        sum_of_products += value * weight
        sum_of_weights += weight
    if sum_of_weights != 0:
        return sum_of_products / sum_of_weights
    else:
        return 0
