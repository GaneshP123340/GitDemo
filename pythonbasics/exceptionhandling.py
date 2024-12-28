# from logging import exception
#
Iteamsincart = 0
# 2 iteams will be added to cart

if Iteamsincart != 2: # raise Exception("product cart count not matching")
    pass
assert(Iteamsincart == 0)


#try , except , finally

try:
    with open('test12.txt', 'r') as reader: # file dose not exist
        reader.read()

# except:
#     print("some how i reached this block because there is failure in try block")

except Exception as e: # standard way of Approach
    print(e)

finally:
    print(" cleaning up resources ")


# try:
#     with open('test.txt', 'r') as reader: # file exist , compiler will not move to except block
#           reader.read()
# except:
#     print("some how i reached this block because there is failure in try block")
# finally:
#     print(" cleaning up resources ") # finally will be excuted in both the case to clean cookies .






