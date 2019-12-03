# Author: Oscar Vallner

def main():
    input_array = []
    with open("input.txt") as input:
        for line in input:
            # Strips line of newline characters, then converts into array of strings
            input_array = line.replace('\n', '').split(',')
            break
    
    num_array = []
    for num in input_array:
        num_array.append(int(num))

    print(num_array)
    position = 0
    op_code = num_array[position]
    while op_code != 99:
        index1 = num_array[position + 1]
        index2 = num_array[position + 2]
        num1 = num_array[index1]
        num2 = num_array[index2]
        destination = num_array[position + 3]
        if op_code == 1:
            num_array[destination] = num1 + num2
            print(f"Position {destination} becomes {num1} + {num2} = {num1 + num2}")
            print(num_array)
        elif op_code == 2:
            num_array[destination] = num1 * num2
            print(f"Position {destination} becomes {num1} * {num2} = {num1 * num2}")
            print(num_array)
        else:
            print("Something went wrong. Invalid op_code")
            break
        position += 4
        op_code = num_array[position]
    print(num_array)

if __name__=="__main__":main()