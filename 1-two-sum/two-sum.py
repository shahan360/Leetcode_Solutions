class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a=[] #create empty list
        # for i in range(len(nums)-1): #running iterator i from index 0 to index n-1
        #     for j in range(i+1,len(nums)): #running iterator j for adjecent element from index 0 to index n 
        #         if nums[i]+nums[j]==target: #comparing summation of values at index i and j with our target values 
        #             a.append(i) #if value at i sums to target, then append the index in array a
        #             a.append(j) #if value at j sums to target, then append the index in array a 
        #             return a #return the array a
        # return a #if nothing found, return the empty array a  

        #solution using hashmap
        prevMap = {} #val:index

        for i,n in enumerate(nums): #collecting index and value from our list array nums
            diff = target-n #the other number of the sum
            if diff in prevMap: #checking if other number in our hashmap
                return [prevMap[diff],i] #then return the indexes of diff and n in a list
            prevMap[n]=i
        return                     