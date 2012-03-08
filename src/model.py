'''
Created on Feb 28, 2012

@author: simshi
'''

class Model(dict):
    digits_ = '123456789'
    row_names_ = '123456789'
    col_names_ = 'ABCDEFGHI'
    all_cells_ = [row + col for row in row_names_ for col in col_names_]
    
    def __init__(self, puzzle_str):
        setter = lambda (k, v):dict.__setitem__(self, k, v in self.__class__.digits_ and v or self.__class__.digits_)
        map(setter, zip(self.__class__.all_cells_, puzzle_str))
        
    def _build_one_triplex(self, row, cols):
        return ' '.join([(len(self[row + col]) == 9 and '?' or self[row + col]).rjust(self._width) for col in cols])
    
    def _build_one_row(self, row):
        return '|'.join([self._build_one_triplex(row, cols) for cols in ('ABC', 'DEF', 'GHI')])
    
    def _build_one_band(self, rows):
        return '\n'.join([self._build_one_row(row) for row in rows])
    
    def __str__(self):
        self._width = max(len(v) == 9 and 1 or len(v) for v in self.itervalues())
        split_line = '\n' + ('+'.join(['-' * (self._width * 3 + 2)] * 3)) + '\n'
        
        bands = [self._build_one_band(rows) for rows in ('123', '456', '789')]
        return split_line.join(bands) + '\n'

    def __repr__(self):
        return "Model(%s)" % self.__str__()
    
    def __getitem__(self, key):
        return dict.__getitem__(self, key)
 
        
