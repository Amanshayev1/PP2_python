path = "/Users/bekasyl2007amanshaevgmail.com/PP2_python/LAB_1/casting.py"  

def count_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

print(count_lines(path))
