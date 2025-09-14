import sys

evenSum = 0
oddSum = 0
even_count = 0
odd_count = 0
min_num = None
max_num = None

input_numbers = sys.argv[1].split(',')  # letting your input to have ,

for arg in input_numbers:
    try:
        nums = int(arg)
    except ValueError:
        print('Please enter valid integers.')
        sys.exit(1)

    if nums % 2 == 0:
        evenSum += nums
        even_count += 1
    else:
        oddSum += nums
        odd_count += 1

    if min_num is None or nums < min_num:
        min_num = nums
    if max_num is None or nums > max_num:
        max_num = nums

total_sum = evenSum + oddSum
centered_average = 0

if even_count + odd_count > 2:
    centered_average = (total_sum - min_num - max_num) / \
        (even_count + odd_count - 2)

# Convert the centered average to an integer
centered_average = int(centered_average)

print('The sum of all even numbers is', str(evenSum) + ', '
      'the sum of all odd numbers is', str(oddSum) + ', '
      'the difference between the biggest and smallest number is', str(
          max_num - min_num) + ', '
      'the total number of even numbers is', str(even_count) + ', '
      'The total number of odd numbers is', str(odd_count) + ', '
      'the centered average is', str(centered_average)+'.')
