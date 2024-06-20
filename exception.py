# myname = "eMobilis"

# for i in myname:
#    if i != "k":


try:
    jina = ('banana', 'apple', 'oranges')
    for i in range(5):
        print(i, jina[i])


except IndexError:
    print(f"Index out of range")
finally:
    print(f"All will be printed")

try:
    # code that might raise exception
    result = 1 / 0
except ZeroDivisionError as e:
    # code to handle exception
    print(f"An error has occurred {e}")
finally:
    # code that runs no matter what
    print("This will always be printed")
