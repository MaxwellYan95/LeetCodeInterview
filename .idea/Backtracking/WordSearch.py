class Solution:
    marked = [];

    def exist(self, board: List[List[str]], word: str) -> bool:
        for out in range(len(board)):
            for inner in range(len(board[out])):
                if board[out][inner] == word[0]:
                    self.marked.append((out, inner));
                    cond = self.findWord(out, inner, board, word[1:len(word)]);
                    self.marked.remove((out, inner));
                    if cond == True:
                        return True;
        return False;
    def findWord(self, outer: int, inner: int, board: List[List[str]], word: str):
        if word == '':
            return True;
        adjCoord = [(outer-1, inner), (outer+1, inner), (outer, inner-1), (outer, inner+1)];
        if outer == 0:
            adjCoord.remove((outer-1, inner));
        if outer == len(board)-1:
            adjCoord.remove((outer+1, inner));
        if inner == 0:
            adjCoord.remove((outer, inner-1));
        if inner == len(board[0])-1:
            adjCoord.remove((outer, inner+1));
        for x, y in adjCoord:
            notContains = (x, y) not in self.marked;
            if notContains:
                element = board[x][y];
                if element == word[0]:
                    self.marked.append((x, y));
                    cond = self.findWord(x, y, board, word[1:len(word)]);
                    self.marked.remove((x, y));
                    if cond == True:
                        return True;
        return False;