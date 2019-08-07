def list_true(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    return result

def mark_false(bool_list, p):
    x = 2 * p
    while x < len(bool_list):
        bool_list[x] = False
        x += p
    return bool_list

def find_next(bool_list, p):
    for i in range(p + 1, len(bool_list)):
        if bool_list[i] == True:
            return i
    return None

def prime_from_list(bool_list):
    result = []
    for i in range(len(bool_list)):
        if bool_list[i]:
            result.append(i)
    return result

def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)