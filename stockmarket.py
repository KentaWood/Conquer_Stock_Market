import sys

def find_longest_non_decreasing_subsequence(prices):
    n = len(prices)
    dp = [1] * n
    prev = [-1] * n
    
    
    
    
    
    

    return #index ? 


def main(infile, outfile):
    with open(infile, 'r') as f:
        days = int(f.readline().strip())
        prices = [int(f.readline().strip()) for _ in range(days)]

    length, subsequence = find_longest_non_decreasing_subsequence(prices)

    with open(outfile, 'w') as f:
        f.write(str(length) + '\n')
        f.write(str(subsequence[0]) + '\n')
        for price in subsequence:
            f.write(str(price) + '\n')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 stockmarket.py infile.txt outfile.txt")
        sys.exit(1)
    
    infile = sys.argv[1]
    outfile = sys.argv[2]
    main(infile, outfile)
