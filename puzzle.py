''' validate_board'''

def validate_rows(board: list) -> bool:
    '''
    Return result of checking rows.
    >>> validate_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
        '''
    pass
def validate_columns(board: list) -> bool:
    '''
    Return result of checking rows.
    >>> validate_columns(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
        '''
    pass

def validate_colors(board: list) -> bool:
    '''
    Return result of checking colored blocks.
    >>> validate_colors(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    if not isinstance(board, list):
        return None
    new_board = []
    for i in range(9):
        new_elem = ''
        for row in range(9-i):
            new_elem += board[row][i]
        new_elem += board[-(i+1)][i+1:]
        new_board.append(new_elem)
    return validate_rows(new_board)

def validate_board(board: list) -> bool:
    '''
    Return result of checking board.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    pass
  
