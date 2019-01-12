
def set_bit(v, index, x):
  mask = 1 << index
  v &= ~mask
  if x:
    v |= mask
  return v


def give_sum_possibiliteies_for_number(input_array, required_sum):
    start = 0
    end = len(input_array) - 1
    res = []
    while(start <= end):
        sum = input_array[start] + input_array[end]
        if sum == required_sum:
            res.append([start, end])
            sum += 1
            end -= 1
        elif sum < required_sum:
            start += 1
        elif sum > required_sum:
            end -= 1
    for index, ele in enumerate(input_array):
        if ele == required_sum:
            res.append([index])
    return res


def solve(bitmask, node, salary_map, input_array):
    possible = False
    number_of_nodes_used = 1
    required_salary_sum = salary_map[input_array[node]]
    possible_subordinates = give_sum_possibiliteies_for_number(input_array, required_salary_sum)
    for subordinates in possible_subordinates:
        number_of_nodes_used = 1
        are_subordinates_avaliable = True
        for index in subordinates:
            if (1<<index)& bitmask != 0:
                are_subordinates_avaliable = False
        if are_subordinates_avaliable:
            possible = True
            for index in subordinates:
                bitmask = bitmask | 1<<index
            for sub_ordinate in subordinates:
                res = solve(bitmask, sub_ordinate, salary_map, input_array)
                possible = possible and res[0]
                number_of_nodes_used += res[1]
            for index in subordinates:
                set_bit(bitmask, index, 0)
        if possible:
            break
    return [possible, number_of_nodes_used]


if __name__ == "__main__":
    t = input()
    input_array = []
    salary_map = dict()
    for i in range(t):
        n = input()
        for j in range(n):
            e, s =list(map(int, raw_input().split(' ')))
            input_array.append(e)
            salary_map[e] = s
    input_array = sorted(input_array)
    a_s = []
    for index, node in enumerate(input_array):
        bitmask = 0
        bitmask = set_bit(bitmask, index, 1)
        res = solve(bitmask, index, salary_map, input_array)
        if res[0]:
            if res[1] == len(input_array):
                a_s.append(node)
        bitmask = set_bit(bitmask, index, 0)
    for ceo in a_s:
        print input_array[ceo]