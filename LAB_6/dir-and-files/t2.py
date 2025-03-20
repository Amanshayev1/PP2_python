import os

path = "/Users/bekasyl2007amanshaevgmail.com/PP2_python/LAB_1"  

def check_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }

print(check_access(path))
