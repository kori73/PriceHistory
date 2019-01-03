def count_pages(func):
    "Decorator to count the number of times a function is called. Used for incrementing the pages."
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        func(*args, **kwargs)
    wrapper.counter = 0
    return wrapper