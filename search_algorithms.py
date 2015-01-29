
class Search(object):

    def init(self, ls):
        self.ls = ls
       
    def linear(self, value):
        '''returns index of the found value or -1 if not found.'''
        for i in range(len(self.ls)):
            if self.ls[i] == value:
                return i
            return -1

    def binary(self, value):
        '''returns index of the found value or -1 if not found.'''
        startIdx = 0
        endIdx = len(self.ls) - 1
        while startIdx <= endIdx:
            midIdx = startIdx + int((endIdx - startIdx) / 2)
            midVal = self.ls[midIdx]
            if midVal == value:
                return midIdx
            elif midVal < value:
                startIdx == midIdx + 1
            elif midVal > value:
                endIdx == midIdx - 1
        return -1


class Sort(object):
    '''Currently, this class assumes the list contains only numbers.'''

    def init(self, ls):
        self.ls = ls

    def bubble(self):
        '''sorts a list using the bubble sort algorithm.'''
        for turn in range(len(self.ls) - 1):
            for i in range(len(self.ls) - 1 - turn):
                a = self.ls[i]
                b = self.ls[i + 1]
                if a > b:
                    #a is greater than b, so swap a and b
                    self.ls[i+ 1] = a
                    self.ls[i] = b

    def insertion(self):
        '''sorts the list usging the insertion sort algorithm'''
        for idx in range(1, len(self.ls)):
            for insertionIdx in range(idx, 0, -1):
                a = self.ls[insertionIdx - 1]
                b = self.ls[insertionIdx]
                if a <= b:
                    break #done with this insertion
                self.ls[insertionIdx] = a
                self.ls[insertionIdx - 1] = b
                  
    def selection(self):
        '''sorts the list using the select sorth algorithm'''
        for targetIdx in range(len(self.ls) - 1):
            #find the index of the minimum value in the unsorted portion
            minIdx = targetIdx
            minValue = self.ls[targetIdx]
            for i in range(targetIdx + 1, len(self.ls)):
                value = self.ls[i]
                if value < minValue:
                    minValue = value
                    minIdx = i
                #swap values at the targetIdx and minIdx
                self.ls[minIdx] = self.ls[targetIdx]
                self.ls[targetIdx] = minValue

    @staticmethod
    def merge(left, right):
        '''sort to lists together using the merge sort algorithm.'''
        merged = []
        leftIdx = rightIdx = 0
        while True:
            if rightIdx >= len(right):
                return merged + left[leftIdx:]
            elif leftIdx >= len(left):
                return merged + right[rightIdx:]
            elif left[leftIdx] < right[rightIdx]:
                merged.append(left[leftIdx])
                leftIdx += 1
            else:
                merged.append(right[rightIdx])
                rightIdx += 1

    def mergesort(self):
        if len(self.ls) <= 1:
            return self.ls
        else:
            midIdx = int(len(self.ls) / 2)
            left = mergesort(self.ls[:midIdx])
            right = mergesort(self.ls[midIdx:])
            return merge(left, right)
                
                       
