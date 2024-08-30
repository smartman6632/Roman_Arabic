# COMP9021 24T1
# Assignment 1 *** Due Monday 25 March (Week 7) @ 9.00am

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


def arabic_to_roman(ara):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman = str()
    i = 0
    while i < len(ara):
        if len(ara) == 4:
            for j in range(int(ara[0])):
                roman += 'M'
            i += 1
        if len(ara) >= 3 and (ara[i] != 0):
            if int(ara[i]) <= 3:
                for j in range(int(ara[i])):
                    roman += 'C'
            elif int(ara[i]) == 4:
                roman += 'CD'
            elif int(ara[i]) == 5:
                roman += 'D'
            elif int(ara[i]) == 9:
                roman += 'CM'
            else:
                roman += 'D'
                for j in range(int(ara[i])-5):
                    roman += 'C'
            i += 1
        if len(ara) >= 2 and (ara[i] != 0):
            if int(ara[i]) <= 3:
                for j in range(int(ara[i])):
                    roman += 'X'
            elif int(ara[i]) == 4:
                roman += 'XL'
            elif int(ara[i]) == 5:
                roman += 'L'
            elif int(ara[i]) == 9:
                roman += 'XC'
            else:
                roman += 'L'
                for j in range(int(ara[i])-5):
                    roman += 'X'
            i += 1
        if len(ara) >= 1 and (ara[i] != 0):
            if int(ara[i]) <= 3:
                for j in range(int(ara[i])):
                    roman += 'I'
            elif int(ara[i]) == 4:
                roman += 'IV'
            elif int(ara[i]) == 5:
                roman += 'V'
            elif int(ara[i]) == 9:
                roman += 'IX'
            else:
                roman += 'V'
                for j in range(int(ara[i])-5):
                    roman += 'I'
        return roman


def roman_to_arabic(rom_ara):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if rom_ara in roman_values:
        return roman_values[rom_ara]
    arabic = 0
    small_index = []
    for i in range(0, len(rom_ara)-1):
        if roman_values[rom_ara[i]] < roman_values[rom_ara[i+1]]:
            small_index.append(i)
    i = 0
    while i < len(rom_ara)-1:
        if i in small_index:
            arabic += roman_values[rom_ara[i+1]] - roman_values[rom_ara[i]]
            i += 2
        else:
            arabic += roman_values[rom_ara[i]]
            i += 1
    if i == len(rom_ara)-1:
        arabic += roman_values[rom_ara[i]]
    if arabic_to_roman(str(arabic)) == rom_ara:
        return arabic


def is_valid_roman(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if len(roman) == 1:
        if roman in roman_values.keys():
            return True
        else:
            return False
    repeat_time = {'I': 0, 'X': 0, 'C': 0}
    previous_char = roman[0]
    if (roman[0] in ['I', 'X', 'C']) and (roman[1] in ['I', 'X', 'C']):
        if roman[0] == roman[1]:
            repeat_time[roman[0]] += 1
    for cur_char_index in range(1, len(roman)):
        if roman[cur_char_index] not in roman_values:
            return False
        if (roman[0] in ['I', 'X', 'C']) and (roman[1] in ['I', 'X', 'C']):
            if roman[0] == roman[1] == 'I':
                repeat_time['I'] += 1
        elif roman[0] == roman[1] == 'X':
            repeat_time['X'] += 1
        elif roman[0] == roman[1] == 'C':
            repeat_time['C'] += 1
        if max(repeat_time.values()) > 3:
            return False
        if roman[cur_char_index] in ['V', 'L', 'D']:
            if previous_char == roman[cur_char_index]:
                return False
        if previous_char in ['V', 'L', 'D']:
            if roman_values[previous_char] < roman_values[roman[cur_char_index]]:
                return False
        if roman_values[roman[cur_char_index]] > 10 * roman_values[previous_char]:
            return False
        previous_char = roman[cur_char_index]
    if (roman_to_arabic(roman) in roman_values.values()) and (roman not in roman_values):
        return False
    return True


def gen_diction(gen_symbol):
    reversed_gen = gen_symbol[::-1]
    newdic = {}
    for i in range(len(reversed_gen)):
        # repeated assign values to the same Roman
        if reversed_gen[i] in newdic:
            return False
        else:
            if i % 2 == 0:
                num_zero = i//2
                newdic[reversed_gen[i]] = '1' + num_zero*'0'
            elif i % 2 == 1:
                num_zero = i//2
                newdic[reversed_gen[i]] = '5' + num_zero*'0'
    return newdic


def arabic_gr(rom_ara, gen_symbol):
    gen_dic = gen_diction(gen_symbol)
    rrom_ara = rom_ara[::-1]
    rom_result = str()
    if not gen_dic:
        return False
    length = len(rom_ara)
    if int(rom_ara[0]) <= 3:
        if len(gen_symbol) < 2*length -1:
            return False
    elif 4 <= int(rom_ara[0]) <= 8:
        if len(gen_symbol) < 2*length:
            return False
    else:
        if len(gen_symbol) < 2*length +1:
            return False
    roman_list = list(gen_dic.keys())
    while length > 0:
        # 1 5 10
        if int(rrom_ara[length-1]) <= 3:
            for i in range(int(rrom_ara[length-1])):
                rom_result += roman_list[2*length-2]
        elif int(rrom_ara[length-1]) == 4:
            rom_result += roman_list[2*length-2] + roman_list[2*length-1]
        elif int(rrom_ara[length-1]) == 5:
            rom_result += roman_list[2*length-1]
        elif int(rrom_ara[length-1]) == 9:
            if roman_list[2*length-1] != roman_list[-1]:
            # 10 part
                bigger_digit = roman_list[2*length]
                rom_result += roman_list[2*length-2] + bigger_digit
            # if the bigger digit is the current biggest digit, and need to have 9, fail to do
            else:
                return False
        else:
            rom_result += roman_list[2*length-1]
            for i in range(int(rrom_ara[length-1])-5):
                rom_result += roman_list[2*length-2]
        length -= 1
    return rom_result


def roman_gr(rom_ara, gen_symbol):
    gen_dic = gen_diction(gen_symbol)
    if not gen_dic:
        return False
    elif rom_ara in gen_dic:
        return gen_dic[rom_ara]
    arabic = 0
    small_index = []
    for i in range(0, len(rom_ara)-1):
        if int(gen_dic[rom_ara[i]]) < int(gen_dic[rom_ara[i+1]]):
            small_index.append(i)
    i = 0
    while i < len(rom_ara) - 1:
        if i in small_index:
            arabic += int(gen_dic[rom_ara[i+1]]) - int(gen_dic[rom_ara[i]])
            i += 2
        else:
            arabic += int(gen_dic[rom_ara[i]])
            i += 1
    if i == len(rom_ara) - 1:
        arabic += int(gen_dic[rom_ara[i]])
    if (not arabic_gr(str(arabic), gen_symbol)):
        return False
    elif arabic_gr(str(arabic), gen_symbol) != rom_ara:
        return False
    else:
        return arabic


def please_convert1(rom_ara):
    # check is valid number
    if rom_ara.isnumeric():
        if rom_ara[0] == '0':
            return "Hey, ask me something that's not impossible to do!"
        elif not ((0 < int(rom_ara) <= 3999)):
            return "Hey, ask me something that's not impossible to do!"
        else:
            return "Sure! It is " + str(arabic_to_roman(rom_ara))
    else:
        if not is_valid_roman(rom_ara):
            return "Hey, ask me something that's not impossible to do!"
        elif not roman_to_arabic(rom_ara):
            return "Hey, ask me something that's not impossible to do!"
        else:
            return "Sure! It is " + str(roman_to_arabic(rom_ara))


def please_convert2(rom_ara, gen_symbol):
    if not gen_symbol.isalpha():
        return "Hey, ask me something that's not impossible to do!"
    if rom_ara.isnumeric():
        if (rom_ara[0] == '0'):
            return "Hey, ask me something that's not impossible to do!"
        # consider whether could transfer in roman successfully
        elif not (arabic_gr(rom_ara, gen_symbol)):
            return "Hey, ask me something that's not impossible to do!"
        else:
            return "Sure! It is " + str(arabic_gr(rom_ara, gen_symbol))
    else:
        if rom_ara.isalpha():
            for i in range(len(rom_ara)):
                if not (rom_ara[i] in gen_symbol):
                    return "Hey, ask me something that's not impossible to do!"
            if not (roman_gr(rom_ara, gen_symbol)):
                return "Hey, ask me something that's not impossible to do!"
            else:
                return "Sure! It is " + str(roman_gr(rom_ara, gen_symbol))


def check_valid(input):
    every_dic = {}
    appear_twice = []
    for i in range(len(input)):
        if input[i] not in every_dic.keys():
            every_dic[input[i]] = 1
        else:
            every_dic[input[i]] += 1
    for key, values in every_dic.items():
        if values == 2:
            appear_twice.append(key)
    for char in appear_twice:
        first_index = input.find(char)
        second_index = input.rfind(char)
        if (second_index - first_index) - 1 == 1:
            if every_dic[input[first_index+1]] != 1:
                return False
        elif (second_index - first_index) - 1 == 2:
            if every_dic[input[first_index+1]] != 1:
                return False
            if every_dic[input[first_index+2]] != 1:
                return False
        elif (second_index - first_index) - 1 > 2:
            return False
    if (max(every_dic.values()) == 3):
        for key, value in every_dic.items():
            if value == 3:
                char_3 = key
        f_index = input.find(char_3)
        if not (input[f_index+1] == char_3 and input[f_index+2] == char_3):
            return False
    if (max(every_dic.values()) == 4):
        for key, value in every_dic.items():
            if value == 4:
                char_4 = key
        f_index = input.find(char_4)
        if not (input[f_index+1] == char_4 and input[f_index+2] == char_4 and every_dic[input[f_index+3]] == 1 and input[f_index+4] == char_4):
            return False
    return True


def mini1(rom):
    rom = list(rom)
    original_rom = list(rom)
    if len(rom)% 2 == 0:
        start = 0
    elif len(rom)% 2 != 0:
        start = 1
    for i in range(start, len(rom)-1, 2):
        rom[i], rom[i+1] = rom[i+1], rom[i]
    original_rom = ''.join(original_rom)
    rom = ''.join(rom)
    return [roman_gr(original_rom, rom), rom]


def gen_diction_3(gen_symbol):
    reversed_gen = gen_symbol[::-1]
    newdic = {}
    for i in range(len(reversed_gen)):
        # repeated assign values to the same Roman
        if reversed_gen[i] == '_':
            continue
        else:
            if i % 2 == 0:
                num_zero = i//2
                newdic[reversed_gen[i]] = '1' + num_zero*'0'
            elif i % 2 == 1:
                num_zero = i//2
                newdic[reversed_gen[i]] = '5' + num_zero*'0'
    return newdic


def roman_gr_3(rom_ara, gen_symbol):
    gen_dic = gen_diction_3(gen_symbol)
    if not gen_dic:
        return False
    elif rom_ara in gen_dic:
        return gen_dic[rom_ara]
    arabic = 0
    small_index = []
    for i in range(0, len(rom_ara)-1):
        if int(gen_dic[rom_ara[i]]) < int(gen_dic[rom_ara[i+1]]):
            small_index.append(i)
    i = 0
    while i < len(rom_ara) - 1:
        if i in small_index:
            arabic += int(gen_dic[rom_ara[i+1]]) - int(gen_dic[rom_ara[i]])
            i += 2
        else:
            arabic += int(gen_dic[rom_ara[i]])
            i += 1
    if i == len(rom_ara) - 1:
        arabic += int(gen_dic[rom_ara[i]])
    return arabic


def mini2(input_sub):
    examples = create(input_sub)
    prev_smallest_key = 0
    for substring in input_sub:
        if len(substring) > 4:
            print('False')
        if len(substring) == 1:
            smallest_key_with_none = min(k for k, v in examples.items() if v is None and k > prev_smallest_key)
            examples[smallest_key_with_none] = substring
            prev_smallest_key = smallest_key_with_none
            # get the smallest which is not assigned to any character
        if len(substring) == 2 and (substring[0] not in examples.values()):
            smallest_key_with_none = min(k for k, v in examples.items() if v is None and k > prev_smallest_key)
            if str(smallest_key_with_none).startswith('5'):
                examples[2*smallest_key_with_none] = substring[0]
            elif str(smallest_key_with_none).startswith('1'):
                examples[smallest_key_with_none] = substring[0]
            prev_smallest_key = smallest_key_with_none
        if len(substring) == 2 and (substring[0] in examples.values()):
            continue
        if len(substring) == 3 and not all_repeated(substring):
            keylist = []
            for k, v in examples.items():
                if v is None and not str(k).startswith('5') and k > prev_smallest_key:
                    keylist.append(k)
            smallest_key_with_none = min(keylist)
            middle_char = substring[1]
            examples[smallest_key_with_none] = middle_char
            prev_smallest_key = smallest_key_with_none
            smallest_key_with_none = min(k for k, v in examples.items() if v is None and not str(k).startswith('5') and k > prev_smallest_key)
            start_char = substring[0]
            examples[smallest_key_with_none] = start_char
            prev_smallest_key = smallest_key_with_none
        if len(substring) == 3 and all_repeated(substring):
            smallest_key_with_none = min(k for k, v in examples.items() if v is None and k > prev_smallest_key)
            if str(smallest_key_with_none).startswith('5'):
                examples[2*smallest_key_with_none] = substring[0]
            elif str(smallest_key_with_none).startswith('1'):
                examples[smallest_key_with_none] = substring[0]
            prev_smallest_key = smallest_key_with_none

        if len(substring) == 4:
            keylist = []
            for k, v in examples.items():
                if v is None and k > prev_smallest_key:
                    keylist.append(k)
            if str(keylist[0]).startswith('5'):
                smallest_key_with_none = keylist[1]
                examples[smallest_key_with_none] = substring[-2]
                smallest_key_with_none = keylist[3]
                examples[smallest_key_with_none] = substring[-1]
                smallest_key_with_none = keylist[4]
                examples[smallest_key_with_none] = substring[1]
            elif str(keylist[0]).startswith('1'):
                smallest_key_with_none = keylist[0]
                examples[smallest_key_with_none] = substring[-2]
                smallest_key_with_none = keylist[2]
                examples[smallest_key_with_none] = substring[-1]
                smallest_key_with_none = keylist[3]
                examples[smallest_key_with_none] = substring[1]
    result = ''.join(["_" if v is None else v for v in examples.values()]).rstrip('_')[::-1]
    return result


def find_substrings(s):
    substrings = []
    # Reverse the string to start searching from the right-hand side
    rs = s[::-1]

    # Find substrings that start and end with the same character
    i = 0
    while i < len(rs):
        char = rs[i]
        same_char = False
        for j in range(i + 1, len(rs)):
            if rs[j] == char:
                substrings.append(rs[i:j+1][::-1])
                same_char = True
                break  # Found the matching end, move to next character
        if same_char:
            i = j+1
        else:
            substrings.append(rs[i][::-1])
            i += 1
    start = 0
    check = 0
    i = 1
    while i < len(substrings):
        if substrings[i] in substrings[check]:
            substrings[check] = 3*substrings[i]
            start += 1
            del substrings[i]
        check += 1
        i += 1
    if start != 0:
        substrings = substrings[:check+1]
        return substrings
    else:
        return substrings


def all_repeated(substring):
    all = substring[0]
    for i in range(1, len(substring)):
        if substring[1] != all:
            return False
    return True


def create(input):
    count = 0
    examples = dict()
    while count <= len(input) * 3:
        if count % 2 == 0:
            num_zero = count // 2
            cur_key = int('1' + '0' * num_zero)
            examples[cur_key] = None
        elif count % 2 != 0:
            num_zero = count // 2
            cur_key = int('5' + '0' * num_zero)
            examples[cur_key] = None
        count += 1
    return examples


def please_convert3(rom):
    if not rom.isalpha():
        return "Hey, ask me something that's not impossible to do!"
    repeated_set = set()
    for char in rom:
        repeated_set.add(char)
    if len(repeated_set) == len(rom):
        return "Sure! It is " + str(mini1(rom)[0]) + ' using ' + mini1(rom)[1]
    elif not check_valid(rom):
        return "Hey, ask me something that's not impossible to do!"
    else:
        substrings = find_substrings(rom)
        mini_2 = mini2(substrings)
        finalized_str = [char for char in mini_2]
        record_dict = dict()
        for i in range(len(rom)):
            if rom[i] not in record_dict:
                record_dict[rom[i]] = 1
            else:
                record_dict[rom[i]] += 1
        keys_list = list(record_dict.keys())
        values_list = list(record_dict.values())
        newdic = gen_diction_3(mini_2)
        i = 0
        while i < len(keys_list)-1:
            if values_list[i] == 1 and values_list[i+1] == 1 and values_list[i+1] != '_' and newdic[keys_list[i]].startswith('5') and finalized_str.index(keys_list[i]) + 1 == finalized_str.index(keys_list[i+1]):
                if (roman_gr_3(keys_list[i+1]+keys_list[i], mini_2) < roman_gr_3(keys_list[i]+keys_list[i+1], mini_2)):
                    finalized_str[mini_2.find(keys_list[i])], finalized_str[mini_2.find(keys_list[i+1])] = finalized_str[mini_2.find(keys_list[i+1])], finalized_str[mini_2.find(keys_list[i])]
                    mini_2 = ''.join(finalized_str)
                    i += 2
                    continue
            i += 1
        finalized_str = ''.join(finalized_str)
        arabic_3 = roman_gr_3(rom, finalized_str)
        return "Sure! It is " + str(arabic_3) + ' using ' + finalized_str




user_in = input('How can I help you? ')
user_input = user_in.split()
if user_input[0] == 'Please' and user_input[1] == 'convert' and len(user_input) == 3:
    print(please_convert1(user_input[2]))
elif user_input[0] == 'Please' and user_input[1] == 'convert' and len(user_input) == 5 and user_input[3] == 'using':
    print(please_convert2(user_input[2], user_input[4]))
elif user_input[0] == 'Please' and user_input[1] == 'convert' and len(user_input) == 4 and user_input[3] == 'minimally':
    print(please_convert3(user_input[2]))
else:
    print("I don't get what you want, sorry mate!")


# EDIT AND COMPLETE THE CODE ABOVE




# DEFINE OTHER FUNCTIONS

#please_convert()
