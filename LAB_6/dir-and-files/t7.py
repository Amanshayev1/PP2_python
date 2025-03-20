def copy_file(src, dest):
    with open(src, "r", encoding="utf-8") as f1, open(dest, "w", encoding="utf-8") as f2:
        f2.write(f1.read())

path = "/Users/bekasyl2007amanshaevgmail.com/PP2_python/LAB_1/casting.py"  
path2 = "/Users/bekasyl2007amanshaevgmail.com/PP2_python/LAB_1/data_types.py"  

copy_file(path, path2)
