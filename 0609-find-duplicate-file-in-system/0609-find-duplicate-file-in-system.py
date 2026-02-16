
class Solution:
    def findDuplicate(self, paths):
        content_map = defaultdict(list)
        
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            
            for file in parts[1:]:
                name, content = file.split("(")
                content = content[:-1]  # remove ")"
                
                full_path = directory + "/" + name
                content_map[content].append(full_path)
        
        result = []
        
        for files in content_map.values():
            if len(files) > 1:
                result.append(files)
                
        return result
