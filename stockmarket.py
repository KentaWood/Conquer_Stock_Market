import sys

def find_longest_non_decreasing_subsequence(prices):
    n = len(prices)
    dp = [1] * n
    prev = [-1] * n

    print(prices)
    
    for i in range(1, n):
        for j in range(i):
            if prices[i] >= prices[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_length = max(dp)
    max_index = dp.index(max_length)

    subsequence = []
    while max_index != -1:
        subsequence.append(prices[max_index])
        max_index = prev[max_index]
        
    print(max_length)
    print(subsequence)

    return max_length, subsequence[::-1]


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
