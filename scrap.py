def the_1880_boys_list():
    all_names = []
    with open('../data/1880-boys.txt', encoding = 'utf-8') as f:
        all_names.extend(f.read().splitlines())
        return all_names

def the_2018_boys_list():
    all_names = []
    with open('../data/2018-boys.txt', encoding='utf-8') as f:
        all_names.extend(f.read().splitlines())
    return all_names

def the_1880_girls_list():
    all_names = []
    with open('../data/1880-girls.txt', encoding='utf-8') as f:
        all_names.extend(f.read().splitlines())
    return all_names

def the_2018_girls_list():
    all_names = []
    with open('../data/2018-girls.txt',encoding='utf-8') as f:
        all_names.extend(f.read().splitlines())
    return all_names
       
def subtract_lists(l1,l2):
    return [x for x in l1 if x not in l2]
    
def names_to_names_boys_to_girls(l1, l2, sort = True):
    dup_list = []
    for item in l1:
        if item in l2:
            dup_list.append(item)

    if sort:
        dup_list.sort()

    return dup_list
    
def main():       
    boys_1880 = the_1880_boys_list()
    boys_2018 = the_2018_boys_list()
    girls_1880 = the_1880_girls_list()
    girls_2018 = the_2018_girls_list()
    
    boys_only_2018 = subtract_lists(boys_2018, girls_2018)
    girls_only_2018 = subtract_lists(girls_2018, boys_2018)
    boys_only_1880 = subtract_lists(boys_1880, girls_1880)
    girls_only_1880 = subtract_lists(girls_1880, boys_1880)

    boys_names_2_girls_names = names_to_names_boys_to_girls(girls_only_2018, boys_only_1880)
    girls_names_2_boys_names = names_to_names_boys_to_girls(boys_only_2018, girls_only_1880)
    
    
    # b_to_g = names_to_names_boys_to_girls(boys_1880,girls_2018)
    # g_to_b = names_to_names_boys_to_girls(girls_1880,boys_2018)
    print(boys_names_2_girls_names)
    print(girls_names_2_boys_names)
    
    
main()