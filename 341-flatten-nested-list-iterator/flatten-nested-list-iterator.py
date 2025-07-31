# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    '''
    Intuition:
    We can use a stack to keep track of the nested lists and flatten them as we iterate through the elements.
    The stack will help us manage the nested structure and allow us to access the next integer efficiently.
    '''

    def __init__(self, nestedList: [NestedInteger]):
        self.flat_list = []
        self._flatten(nestedList)
        self.index = 0

    def _flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.flat_list.append(item.getInteger())
            else:
                self._flatten(item.getList())

    def next(self) -> int:
        result = self.flat_list[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.flat_list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())