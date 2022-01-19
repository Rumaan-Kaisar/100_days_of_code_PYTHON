# Different Errors

# FileNotFoundError
try:
    file = open("test_exception.txt")
    
    # Following error will be skipped
    demo_dict = {"key" : "value"}
    value = demo_dict["text"]

except FileNotFoundError:
    print("File does not exist. New file Crated")
    file = open("test_exception.txt", "a")
    file.write("something")
except KeyError as err_msg:
    print(f"Key {err_msg} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed")
# # KeyError
# demo_dict = {"key" : "value"}
# value = demo_dict["text"]

# # IndexError
# demo_list = ["peach", "apple", "orange"]
# fruit = demo_list[3]

# # TypeError
# text = "abc"
# num = text + 6



# python exception_demo.py