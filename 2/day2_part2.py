# Author: Oscar Vallner

def find_output(num_array, noun, verb):
    num_array[1] = noun
    num_array[2] = verb 

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
        elif op_code == 2:
            num_array[destination] = num1 * num2
        else:
            print("Something went wrong. Invalid op_code")
            break
        position += 4
        op_code = num_array[position]
    
    return num_array[0]

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
    master_array = num_array.copy()

    output = 0
    for noun in range(0, 100):
        for verb in range(0, 100):
            output = find_output(num_array, noun, verb)
            if output == 19690720:
                print(f"Noun is: {noun} and Verb is: {verb}")
            # Need to reset the array to its original state!
            num_array = master_array.copy()

if __name__=="__main__":main()