'''
Created on Feb 28, 2012

@author: simshi
'''

class Model(dict):

    def _build_one_triplex(self, row, cols):
        return ' '.join([self[row + col].rjust(self._width) for col in cols])
    
    def _build_one_row(self, row):
        return '|'.join([self._build_one_triplex(row, cols) for cols in ('ABC', 'DEF', 'GHI')])
    
    def _build_one_band(self, rows):
        return '\n'.join([self._build_one_row(row) for row in rows])
    
    def __str__(self):
        self._width = len(self) > 0 and max(len(v) for v in self.itervalues()) or 1
        split_line = '\n' + ('+'.join(['-'*(self._width * 3 + 2)] * 3)) + '\n'
        
        bands = [self._build_one_band(rows) for rows in ('123', '456', '789')]
        return split_line.join(bands) + '\n'

    def __repr__(self):
        return "Model(%s)" % self.__str__()
    
    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return '?'
        
