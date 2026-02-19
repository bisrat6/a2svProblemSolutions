class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        current_line = []
        in_block_comment = False
        
        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if in_block_comment:
                    if i + 1 < n and line[i] == '*' and line[i + 1] == '/':
                        in_block_comment = False
                        i += 1
                    i += 1
                else:
                    if i + 1 < n and line[i] == '/' and line[i + 1] == '*':
                        in_block_comment = True
                        i += 1
                    elif i + 1 < n and line[i] == '/' and line[i + 1] == '/':
                        break
                    else:
                        current_line.append(line[i])
                    i += 1
            
            if not in_block_comment and current_line:
                result.append(''.join(current_line))
                current_line = []
        
        return result
