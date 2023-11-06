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
    pass

def validate_board(board: list) -> bool:
    '''
    Return result of checking board.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    if not isinstance(board, list):
        return None
    return validate_rows(board) and validate_columns(board) and validate_colors(board)pass
  
