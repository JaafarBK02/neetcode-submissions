class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)
        

        for c in range(9):
            seen2 = set()
            for r in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                
                if value in seen2:
                    return False

                seen2.add(value)

        for box_r in range (0,9,3):
            for box_c in range(0,9,3):
                seen3 = set()
                
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        value = board[r][c]

                        if value == '.':
                            continue
                        
                        if value in seen3:
                            return False
                        
                        seen3.add(value)
        

        return True





            










        




        