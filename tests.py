# =====
# =====
# =====

# from functions.get_files_info import get_files_info

# result1 = get_files_info("calculator", ".")
# print(result1)

# result2 = get_files_info("calculator", "pkg")
# print(result2)

# result3 = get_files_info("calculator", "/bin")
# print(result3)

# result4 = get_files_info("calculator", "../")
# print(result4)

# =====
# =====
# =====

# from functions.get_file_content import get_file_content

# result1 = get_file_content("calculator", "main.py")
# print(result1)

# result2 = get_file_content("calculator", "pkg/calculator.py")
# print(result2)

# result3 = get_file_content("calculator", "/bin/cat")
# print(result3)

# result4 = get_file_content("calculator", "pkg/does_not_exist.py")
# print(result4)

# =====
# =====
# =====

# from functions.write_file import write_file

# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

# =====
# =====
# =====

from functions.run_python_file import run_python_file

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))
print(run_python_file("calculator", "lorem.txt"))
