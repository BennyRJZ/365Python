# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples
#  of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = list(range(1,n+1))
        result = []
        for number in a:
            if number%3 == 0 and number%5 == 0:
                number = "FizzBuzz"
                result.append(number)
            elif number%3 == 0:
                number = "Fizz"
                print(number)
                result.append(number)
            elif number%5 == 0:
                number = "Buzz"
                print(number)
                result.append(number)
            else:
                number = str(number)
                result.append(number)
        
        a = map(str,a)
        print(result)
        return(result)