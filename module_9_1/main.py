
def apply_all_func(int_list,*functions):
    result = {}
    for func in functions:
        result[str(func.__name__)] = func(int_list)
        return result

print(apply_all_func([5,30,14,9],max))
print(apply_all_func([5,30,14,9],min))
print(apply_all_func([5,30,14,9],len))
print(apply_all_func([5,30,14,9],sum))
print(apply_all_func([5,30,14,9],sorted))
