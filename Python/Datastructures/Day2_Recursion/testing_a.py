def my_str():
    message = "python"
    new_msg = message + " is " + message
    print(new_msg.replace(message,"fff"))
    return new_msg

print(my_str())