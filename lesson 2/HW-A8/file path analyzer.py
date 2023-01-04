path = input("insert path: ")
valid = 1

if path.find(':\\') == 1 and path[0].isupper():
    path_split = path.split("\\")
    if "." in path_split[-1]:
        print(f"depth of the path is {len(path_split) - 2}")
        file_split = path_split[-1].split(".")
        print(f"the file name is: {file_split[0]}")
        print(f"the extension of the file is: .{file_split[1]}")
    else:
        print("error")

elif path[0] == '/':
    path_split = path.split("/")
    if "." in path_split[-1]:
        print(f"depth of the path is {len(path_split) - 2}")
        file_split = path_split[-1].split(".")
        print(f"the file name is: {file_split[0]}")
        print(f"the extension of the file is: .{file_split[1]}")
    else:
        print("error")

else:
    print("error")

