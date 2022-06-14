import re


def tweets_netflix():
    """splits all lines in the input files into date and tweet, and counts the amount of times the search term occurs before and after march 15 2020."""

    files = ['n12.txt', 'n01.txt', 'n02.txt', 'n03.txt', 'n04.txt', 'n05.txt', 'n06.txt']

    searchterms = re.compile(r"netflix")

    before_total = 0
    after_total = 0
    before_found = 0
    after_found = 0

    for n in files:
        with open(n, 'r', encoding='utf-8') as inp:
            file = inp.readlines()
        for line in file:
            line = line.rstrip().split('\t')

            date = line[0].split()[0]
            date1 = date.split('-')
            tweet = line[1]

            if date1[1] in ['12','01','02']:
                before_total += 1
                if searchterms.search(tweet.lower()) is not None:
                    before_found += 1
            elif date1[1] == '03' and int(date1[2]) <= 15:
                before_total += 1
                if searchterms.search(tweet.lower()) is not None:
                    before_found += 1
            else:
                after_total += 1
                if searchterms.search(tweet.lower()) is not None:
                    after_found += 1

    return [before_total, before_found, after_total, after_found]


def main():
    results = tweets_netflix()

    print("________________________________________________________")
    print("{:^54}".format("01-12-2019 - 15-03-2020:"))
    print("Total: {0}".format(results[0]))
    print("Tweets containing search terms: {0}".format(results[1]))
    print()
    print("Percentage: {0}%".format(round(((results[1]/results[0])*100), 2)))
    print("________________________________________________________")
    print("{:^54}".format("16-03-2020 - 30-06-2020:"))
    print("Total: {0}".format(results[2]))
    print("Tweets containing search terms: {0}".format(results[3]))
    print()
    print("Percentage: {0}%".format(round(((results[3]/results[2])*100), 2)))
    print("________________________________________________________")


if __name__=="__main__":
    main()