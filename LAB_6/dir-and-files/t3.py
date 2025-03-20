import os

path = "/Users/bekasyl2007amanshaevgmail.com/PP2_python/LAB_1"  

def path_info(path):
    if os.path.exists(path):
        return {"directory": os.path.dirname(path), "filename": os.path.basename(path)}
    return "Path does not exist"

print(path_info(path))
