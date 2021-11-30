n = int(input("Enter the size of the list1 "))
lt1 = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:n]
n = int(input("Enter the size of the list2 "))
lt2 = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:n]
print(" Python list 1 : " , lt1)
print("Python list 2 : " ,lt2)
res_lt = [lt1[x] + lt2[x] for x in range(len(lt1))]
print(" Addition of the list lt1 and lt2 is: " + str(res_lt))