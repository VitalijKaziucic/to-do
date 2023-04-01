def read_file(file_name: str) -> list:
    """
    Function reads data from provided txt file
    :param file_name:
    :return list of data:
    """
    try:
        with open(file_name, mode='r') as readFile:
            return readFile.readlines()
    except FileNotFoundError:
        file = open(file_name, mode='x')
        file.close()
        return read_file(file_name)
