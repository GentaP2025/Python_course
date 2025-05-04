from random import randrange
num_runs = 1000

def rolling():
    D1 = randrange(1,7)
    D2 = randrange(1,7)
    tot = D1+D2
    return tot

def main():
    expected_proportions= {2:1/36, 3:2/36, 4:3/36, 5:4/36, 6:5/36, 7:6/36, 8:5/36, 9:4/36, 10:3/36, 11:2/36, 12:1/36}
    count_proportions = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

    for i in range(1,num_runs+1):
        a=rolling()
        count_proportions[a] += 1
           

    for i in sorted(count_proportions.keys()):
        count = count_proportions[i]
        observed_percentage = round((count / num_runs) * 100,2)
        expected_percentage = round(expected_proportions[i] * 100,2)
        print(i, count, observed_percentage,expected_percentage)
        

main()
