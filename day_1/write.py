def write_file(file_name: str, data: list) -> None:
    """
    Function writes data to txt file
    :param file_name:
    :param data:
    :return None:
    """
    with open(file_name, "w") as writeFile:
        writeFile.writelines(data)
