def add_before_ui_after_ui(func):
    def wrapper():
        print("Before running the test")
        print("Start the browser")
        func()
        print("Ending the test")
        print("Quit the browser")
    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print("I will start testing")