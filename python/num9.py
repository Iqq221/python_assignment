# Convert string "Hello$World" into Base64
import base64
str="Hello$World"
str_bytes=str.encode("utf-8")
base64_bytes=base64.b64encode(str_bytes)
base64_str=base64_bytes.decode("utf-8")
print(f"string is - {str}")
print(f"base64 string is - {base64_str}")