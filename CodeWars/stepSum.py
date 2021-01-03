# Your task is to make function, which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step.

# If begin value is greater than the end, function should returns 0

# Examples

# sequenceSum(2,2,2) === 2
# sequenceSum(2,6,2) === 12 // 2 + 4 + 6
# sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
# sequenceSum(1,5,3) === 5 // 1 + 4


def sequence_sum(begin_number, end_number, step):
    begin = begin_number
    end = end_number
    stp = step
    result = 0
    for x in range (begin,end+1,step):
        result = x + result
    
    return result
        