from re import sub
import sys

def find_longest_non_decreasing_subsequence(prices):
    
    def helper(prices):
        if len(prices) <= 1:
            return len(prices), prices

        mid = len(prices) // 2
        left_length, left_subsequence = helper(prices[:mid])
        right_length, right_subsequence = helper(prices[mid:])

        # Find the longest streak that crosses both arrays
        i = mid - 1
        j = mid
        mid_streak = 1

        if prices[i] <= prices[j]:
            # If the middle elements form a streak
            mid_streak = 2

            # Find the length of the streak to the left
            while i >= 1 and prices[i] <= prices[i+1]:
                mid_streak += 1
                i -= 1

            # Find the length of the streak to the right
            j = mid + 1
            while j < len(prices) and prices[j] >= prices[j-1]:
                mid_streak += 1
                j += 1

        # Determine the longest length and its corresponding subsequence
        max_length = max(left_length, mid_streak, right_length)
        if max_length == left_length:
            return len(left_subsequence), left_subsequence
        elif max_length == mid_streak:
            return len(prices[i+1:j]), prices[i+1:j]
        else:
            return len(right_subsequence), right_subsequence
    
    return helper(prices)

def find_first_index(main_array, sub_array):
    for i in range(len(main_array)):
        if main_array[i:i+len(sub_array)] == sub_array:
            return i + 1

def main(infile, outfile):
    with open(infile, 'r') as f:
        days = int(f.readline().strip())
        prices = [int(f.readline().strip()) for _ in range(days)]

    
    length, subsequence = find_longest_non_decreasing_subsequence(prices)
    index = find_first_index(prices, subsequence)
    
    print(length)
    print(index)
    print(subsequence)
    

    with open(outfile, 'w') as f:
        f.write(str(length) + '\n')
        f.write(str(index) + '\n')
        for price in subsequence:
            f.write(str(price) + '\n')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 stockmarket.py infile.txt outfile.txt")
        sys.exit(1)
    
    infile = sys.argv[1]
    outfile = sys.argv[2]
    main(infile, outfile)
