
dict_key = input("Click the return(enter) key on your device")
final_dict = {}

while dict_key != "Done":

    dict_key = input("Enter the name of the Key> ")
    if dict_key == "Done":
        exit()
    else:
        dict_value = input("Enter the name of the value> ")
        final_dict[dict_key] = dict_value


print("Dictionary formed: ", final_dict)
