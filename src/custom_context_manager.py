class CustomContextManager:
    def __init__(self, filename, mode) -> None:
        print("Init...")
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Entering...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exiting...")
        self.file.close()


with CustomContextManager('test.txt', 'r+') as fp:
    pass

