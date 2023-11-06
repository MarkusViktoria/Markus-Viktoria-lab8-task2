''' validate_board'''

def validate_rows(board: list) -> bool:
    '''
    Return result of checking rows.
    >>> validate_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
        '''
    if not isinstance(board, list):
        return None
    for rows in board:
        for elem in rows:
            if rows.count(elem) != 1 and elem.isdigit():
                return False
    return True
    
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
    pass
  
