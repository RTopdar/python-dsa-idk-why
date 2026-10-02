number=1248
number_backup = number
print(f"Number of numbers that can divivde the number {number} are {sum(1 for i in range(1, number) if number% i ==0)}")

while(number>0):
    last_dig = number%10
    print(f"{number_backup} is divisible by {last_dig}") if number_backup % last_dig == 0 else print("No divisible")
    number = number // 10