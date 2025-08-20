#Write a program to ask the user to which browser he want to run the automation
browser_name = input("Enter your browser name: ")
match browser_name:
    case "firefox":
        print("Run Firefox")
    case "chrome":
        print("Run Chrome")
    case "safari":
        print("Run Safari")
    case _:
        print("Invalid browser name")