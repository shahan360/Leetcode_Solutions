class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #write your code here
        if len(nums) > 1: # Yeh base case hai, agar array ki length 1 se zyada hai toh hum merge sort karenge (This is the base case, if the length of the array is greater than 1, we will perform merge sort)
            mid = len(nums) // 2  # array ke beech ka index nikalna (Finding the middle index of the array)
            L = nums[:mid]        # Left half of the array jismain starting se lekar mid tak ke elements hain (Left half of the array which contains elements from the start to mid)
            R = nums[mid:]        # Right half of the array jismain mid se lekar end tak ke elements hain (Right half of the array which contains elements from mid to end)

            self.sortArray(L)         # humne recursive call kiya hai left half ke liye jo ki merge sort karega (We have made a recursive call for the left half which will perform merge sort)
            self.sortArray(R)         # humne recursive call kiya hai right half ke liye jo ki merge sort karega (We have made a recursive call for the right half which will perform merge sort)

            i = j = k = 0        # i, j, k ko 0 se initialize kiya hai kyunki humne arrays L aur R ke elements ko compare karna hai (Initialized i, j, k to 0 because we will compare the elements of arrays L and R)
            # i is the index for L[], j is the index for R[] and k is the index for arr[]

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R): # Yeh loop tab tak chalega jab tak L aur R ke elements khatam nahi ho jate (This loop will run until the elements of L and R are exhausted)
                if L[i] < R[j]: # Agar L ka element R se chhota hai toh hum L ka element arr mein daalenge (If the element of L is smaller than R, we will put the element of L in arr)
                    nums[k] = L[i] # arr mein L ka element daalna (Putting the element of L in arr)
                    i += 1 # L ka index badhana (Incrementing the index of L)
                else: # Agar R ka element L se chhota hai toh hum R ka element arr mein daalenge (If the element of R is smaller than L, we will put the element of R in arr)
                    nums[k] = R[j] # arr mein R ka element daalna (Putting the element of R in arr)
                    j += 1 # R ka index badhana (Incrementing the index of R)
                k += 1 # arr ka index badhana (Incrementing the index of arr)

            # Checking if any element was left in L[] or R[]
            # Agar L ya R mein koi element bacha hai toh hum usse arr mein daalenge (If there are any elements left in L or R, we will put them in arr
            while i < len(L): # Agar L mein koi element bacha hai toh hum usse arr mein daalenge (If there are any elements left in L, we will put them in arr)
                nums[k] = L[i] # arr mein L ka element daalna (Putting the element of L in arr)
                i += 1 # L ka index badhana (Incrementing the index of L)
                k += 1 # arr ka index badhana (Incrementing the index of arr)

            while j < len(R): # Agar R mein koi element bacha hai toh hum usse arr mein daalenge (If there are any elements left in R, we will put them in arr)
                nums[k] = R[j] # arr mein R ka element daalna (Putting the element of R in arr)
                j += 1 # R ka index badhana (Incrementing the index of R)
                k += 1 # arr ka index badhana (Incrementing the index of arr)
        return nums        