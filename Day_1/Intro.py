def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    x = 'Aayush'
    s = "Hi, {}"
    print(s.format(x))
    s = "Hi, {} and {}"
    print(s.format(x,100))
    s = "Hi, {1} and {0}"
    print(s.format(x,100))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

