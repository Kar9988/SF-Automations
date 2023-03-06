from selenium import webdriver
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.org/")
query = driver.find_element("id", "searchInput")
query.send_keys("Hello World")
query.submit()
print(driver.find_element("id", "firstHeading").text)
assert driver.title == "\"Hello, World!\" program - Wikipedia"
driver.close()
