from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_map = defaultdict(list)  # key: file content, value: list of file paths
        
        for path in paths:
            parts = path.split(" ")
            dir_path = parts[0]  # first part is the directory
            
            for file in parts[1:]:
                # split file name and content
                name, content = file.split("(")
                content = content[:-1]  # remove trailing ')'
                
                # store full path
                full_path = f"{dir_path}/{name}"
                content_map[content].append(full_path)
        
        # only return lists with 2 or more files (duplicates)
        return [files for files in content_map.values() if len(files) > 1]