class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # m column ki length hai
        if m == 0: # agar column ki length 0 hai toh result false hoga 
            return False
        n = len(matrix[0]) # n matrix ki pehli row ki length hai

        # ab hum binary search laggayenge
        baanya = 0
        daanya = m * n - 1
        while baanya <= daanya:
            beenchka = (baanya+daanya)//2
            column_ka_index = beenchka // n
            column_ke_row_ka_index = beenchka % n
            ye_waala = matrix[column_ka_index][column_ke_row_ka_index]
            if  ye_waala == target:
                return True
            else:
                if ye_waala > target:
                    daanya = beenchka - 1
                else:
                    baanya =beenchka + 1
        return False                     

        