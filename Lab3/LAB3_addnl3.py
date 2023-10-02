
def outer_function():
    print("outer fn.")

    def inner_function():
        print("inner fn.")

    inner_function()

outer_function()
