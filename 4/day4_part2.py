
def main():
    valid_passwords = []
    range_min = 130254
    range_max = 678275

    for password in range(range_min, range_max + 1):
        contains_double = False
        always_increasing = True
        prev_digit = -1
        prev_prev_digit = -1
        for digit in str(password):
            if int(digit) < prev_digit:
                always_increasing = False
            if prev_digit == int(digit):
                if prev_digit != prev_prev_digit:
                    contains_double = True
                else:
                    contains_double = False
            prev_prev_digit = prev_digit
            prev_digit = int(digit)
            print(f"prev prev: {prev_prev_digit}")
            print(f"prev: {prev_digit}")
        break

        if always_increasing and contains_double:
            valid_passwords.append(password)

    print(f"num valid: {len(valid_passwords)}")

if __name__=="__main__":main()
