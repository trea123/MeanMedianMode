"""Module containing logic for calculating the mean, median, and mode of a data set."""


def main(debug: bool = False) -> bool:
    """
    Execute the main process.

    This function is used to test the functionality of the entire module.  It will include hard-coded data sets in the form of Python list objects containing integers.  These data set objects will be passed to a 'solve all' method that will determine each data set's mean, median, and mode.  The return value for each of the function calls, utilizing the data sets, will be a tuple.  Each return tuple will be printed to show that the solution is working properly.
    
    Args:
        debug (bool): A flag representing whether the function runs in debug mode or not.

    Returns:
        bool: The return status for the execution of the main process.

    """

    print("[*] Starting.")

    if debug:
        print("[!] Running in debug mode.")

    data_set_1 = [6, 9, 1, 2, 6, 3, 7]
    data_set_2 = [6, 9, 1, 2, 6, 3, 7, 4]
    data_set_3 = [6, 9, 1, 2, 6, 3, 7, 4, 1]
    data_set_4 = [6, 9, 1, 2, 3, 7, 4]

    print("[*] Finished.")
    
    return True


if __name__ == "__main__":
    if not main():
        raise Exception("[!] Error running main function.")
