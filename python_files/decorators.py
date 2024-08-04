def announce(f):
    def wrapper():
        print("About to run the funciton.")
        f()
        print("Done running the function.")

