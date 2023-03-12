def palindrome(arr):
  lastIndex = len(arr) - 1
  firstIndex = 0
  while (firstIndex < lastIndex):
    if (arr[firstIndex] != arr[lastIndex]):
      return False
    firstIndex += 1
    lastIndex -= 1
  return True


      