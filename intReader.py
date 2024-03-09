total = 0 
count = 0
avg = 0


while True:
    try:
        user = input("Enter a number: ")
        if user == "done":
            break
        else:
            print(user)
            user = int(user)
            total = total + user
            count =  count + 1
            avg = total/count
    except:
        print("Invalid Input")
        continue
    
    
print(f"Total: {total}, Count: {count}, Average: {avg}")