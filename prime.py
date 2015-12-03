
def get_num_list(limit):
    num_list = []
    for i in range(2,(limit+1)):
        num_list.append(i)
    return num_list

def pop(num_list,multiple):
    for i in range(31):
        if multiple == num_list[i]:
            num_list.pop(i)
    return num_list

def compute_prime(limit):
    num_list = get_num_list(limit)
    prime_list = [] 
    for i in num_list:
        for j in range(2,16):
            try:
                multiple = i*j
                prime_list = num_list
                num_list = pop(num_list,multiple)
                #prime_list = num_list  -->if prime_list is given here the output is none, why?
            except IndexError:
                continue
    return prime_list

def main():
    limit = 30
    prime_list =[]
    prime_list = compute_prime(limit)
    print prime_list

if __name__ == "__main__":
    main()
    

