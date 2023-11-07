
def getFizzBuzz(num):
    result = num

    if num % 3 == 0 and num % 5 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"

    return result

def main(num = None):
    if num == None:
        num = int(input("Enter a number: "))

    result = getFizzBuzz(num)
    print(result)

    #for num in range(1, 101):
        #print(getFizzBuzz(num))
    return result

if __name__ == '__main__':
    main()
    
