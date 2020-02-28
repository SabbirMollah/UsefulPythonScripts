import re


file = open("source_code.bf")
source_code = ""

for line in file.readlines():
    source_code+=line


source_code = re.sub(r"\s+", "", source_code, flags=re.UNICODE)
# print(source_code)

source_code_index = 0
source_code_loop_stack = []

program_array = [0 for _ in range(15)]
pointer = 0

while source_code_index < len(source_code):
    char = source_code[source_code_index]
    #print("Source Index",source_code_index,"Char:",char,"Pointer",pointer,"Program Array:",program_array, "Loop Stack", loop_stack, "Source Stack", source_code_loop_stack)
    if char == '>':
        pointer += 1

    elif char == '<':
        pointer -= 1
        
    elif char == '+':
        program_array[pointer] += 1

    elif char == '-':
        program_array[pointer] -= 1

    elif char == '.':
        print(chr(program_array[pointer]),end='')

    elif char == ',':
        program_array[pointer] = int(input())

    elif char == '[':
        if program_array[pointer] == 0:
            paren_count = 0
            while source_code[source_code_index] != "]":
                source_code_index +=1
                if source_code[source_code_index] == "[":
                    paren_count+=1
                if source_code[source_code_index] == "]":
                    if paren_count == 0:
                        break
                    else:
                        paren_count -= 1
        else:
            source_code_loop_stack.append(source_code_index+1)


    elif char == ']':
        source_code_stack_top = source_code_loop_stack.pop()

        if program_array[pointer] != 0:
            source_code_loop_stack.append(source_code_stack_top)
            source_code_index = source_code_stack_top
            continue

    source_code_index += 1

