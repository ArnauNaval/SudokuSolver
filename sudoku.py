import numpy as np
import copy

class Sudoku:
    @staticmethod
    def read_from(path_to_file):
        """
        Given a file, obtain a sudoku object
        """
        sudoku = np.zeros((9,9))
        with open(path_to_file, 'r') as f:
            i = 0
            for line in f.readlines():
                sudoku[i,:] = np.array(list(line.split('\n')[0]), dtype='uint8')
                i+=1
        return sudoku


    def __init__(self, fname):
        self._sudoku = Sudoku.read_from(fname)
        
    def __str__(self):
        _str = ""
        for i in range(9):
            if i%3 == 0:
                _str += "+-------+-------+-------+\n"
            xx = tuple([str(int(x)) if x != 0 else ' ' for x in self._sudoku[i, :]])
            _str += "| %s %s %s | %s %s %s | %s %s %s |\n"  % xx
        _str += "+-------+-------+-------+\n"
        
        return _str
    
    def get_valid(self, pos):
        if self._sudoku[pos] != 0:
            return []
        _all = [x for x in range(1,10)]
        row = self._sudoku[pos[0], :]
        column = self._sudoku[:, pos[1]]
        block = (int(pos[0]/3), int(pos[1]/3))
        block = np.ravel(self._sudoku[block[0]*3:block[0]*3+3,block[1]*3:block[1]*3+3])
        
        _all = np.array([x for x in _all if x not in row and x not in column and x not in block])
        return _all
        
    def set_number(self, pos, number):
        if number in self.get_valid(pos):
            s = copy.deepcopy(self)
            s._sudoku[pos] = number
            return s
        return self
    
    def get_empty(self):
        x, y = np.where(self._sudoku==0)
        return [(x[i],y[i]) for i in range(len(x)) ]