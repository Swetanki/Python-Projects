def count_substring(string, sub_string):
    count = 0
    substr = len(sub_string)

    for i in range(len(string)):
        if string[i:i + substr] == sub_string:
            count += 1

    return count

if __name__ == '__main__':
    string = "abracadabraabracadabra"
    sub_string = "bra"
    
    count = count_substring(string, sub_string)
    print(count)