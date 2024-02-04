# Definition for an integer array reader.
class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        if index < len(self.arr):
            return self.arr[index]
        else:
            return float('inf')

class Solution:
    def search(self, reader, target):
        #We initialize two variables 'start' and 'end' to help us search in the array
        start, end = 0, 10000

        #We use a 'while' loop to keep searching until we find the target or narrow down the search range
        while start + 1 < end:
            #We calculate the middle index of the current search range
            mid = start + (end - start) // 2

            #We check if the target is equal to the value at the middle index
            if target == reader.get(mid):
                #if it is, we found the target, and we return the index
                return mid
            #If the target is smaller than the value at the middle index
            elif target < reader.get(mid):
                #We update the 'end' to narrow down the search range to the left half
                end = mid - 1
            #If the target is larget than the value at the middle index
            else:
                #We update the 'start' to narrow down the search range to the right half
                start = mid + 1

        #After the 'while' loop, we check if the target is at the 'start' or 'end' index
        if reader.get(start) == target:
            #If it is, we return the 'start' index as we found the target
            return start
        elif reader.get(end) == target:
            #If it is at 'end', we return the 'end' index as we found the target
            return end

        #If the target is not found in the array, we return -1
        return -1  
                     


# Driver code
if __name__ == "__main__":
    #Example usage:
    arr = [1, 4, 6, 8, 10, 15, 20]
    target = 8

    array_reader = ArrayReader(arr)
    solution = Solution()
    result = solution.search(array_reader, target)

    if result != -1:
        print(f"Target {target} found at index {result}")
    else:
        print(f"Target {target} not found in the array")