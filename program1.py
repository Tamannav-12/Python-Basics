def reverse_integer (n:int) -> int:
    sign=-1 if n < 0 else 1
    a = abs(n)
    rev = int(str(a)[::-1])
    return sign*rev

if __name__=="__main__":
    x = int(input("Enter an integer:"))
    print("Reversed integer:",reverse_integer(x))
        