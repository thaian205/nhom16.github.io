a= float(input("Nhập số cần tính căn bậc hai: "))
guess=a/2
while abs(guess*guess-a) > 10**(-12):
    guess = (guess+a/guess)/2
print("Căn bậc hai của", a, "là", guess)