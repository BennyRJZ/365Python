# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.
def make_readable(seconds):
    #DIVMOD, a = division, b = remainder. 
    min, sec = divmod(seconds,60)
    
    hr, min = divmod(min,60)
    
    print(f"{min}  {sec}")
    print(f"{hr}  {min}")
    result = f"{hr:02d}:{min:02d}:{sec:02d}"
    return(result)
