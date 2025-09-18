import time
import pyfiglet
import sys

# Tạo chữ nghệ thuật bằng ASCII
ascii_banner = pyfiglet.figlet_format("Hello World!")

# In từng ký tự với hiệu ứng typing
for char in ascii_banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.002)  # chỉnh tốc độ (giảm số nhỏ để nhanh hơn)
