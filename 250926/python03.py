import sys

original_stdout = sys.stdout
file_path = ".\\log_test.txt"
log = open(file_path, "w")

sys.stdout = log
print("hello world")

sys.stdout = original_stdout
print("printing at console")