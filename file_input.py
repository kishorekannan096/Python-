def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
      for j in range(0, n-i-1):
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]

def read_numbers_from_file(file_path):
  with open(file_path, "r") as file:
      lines = file.readlines()
      numbers = [int(line.strip()) for line in lines]
  return numbers

def main():
  file_path = "numbers.txt"
  numbers = read_numbers_from_file(file_path)
  print("Original list of numbers:", numbers)
  bubble_sort(numbers)
  print("Sorted list of numbers:", numbers)

main()
