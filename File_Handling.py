from pathlib import Path  # Import the pathlib module to manipulate filesystem paths


class FileHandling:

    def __init__(self):
        self.__file_name = ''
        self._social_NW = {}
        self._number_of_users = 0
        self.__temporary_NW_list = []
        # Creating a temporary attribute help avoid reading the file multiple times.

    # This method check if the file exists
    def check_file_name(self, file_name):
        self.__file_name = Path(file_name)  # Using Path class convert user input to filesystem path
        while not self.__file_name.is_file():
            self.__file_name = Path(input('File not supported. Try another file or exit (n):'))
            if str(self.__file_name) in ('n', 'N'):
                return False
        return True

    # Read the data from file and store it in a temporary list
    def read_data_from_file(self):
        with open(self.__file_name) as file:
            self._number_of_users = int(file.readline())
            for line in file:
                line_values = line.split()
                self.__temporary_NW_list.append(line_values)
        file.close()

    # Read the data from temporary list and add keys to the network dictionary
    def assign_keys(self):
        for element in self.__temporary_NW_list:
            for value in element:
                self._social_NW[value] = []

    # Read the data from temporary list and add values to the network dictionary
    def assign_values(self):
        for element in self.__temporary_NW_list:
            if len(element) > 1:
                for value in element:
                    if element[0] is value:
                        self._social_NW.setdefault(element[0], []).append(element[1])
                    elif element[1] is value:
                        self._social_NW.setdefault(element[1], []).append(element[0])
                    else:
                        print('Something went wrong')

    # Check the consistency of the network
    def check_consistency(self):
        for element in self.__temporary_NW_list:
            if len(element) == 1:
                for index in range(self._number_of_users):
                    user_friends = list(self._social_NW.values())[index]
                    if element[0] in user_friends:
                        self._social_NW[element[0]] = []
                        print('The network is inconsistent, try another file.')
                        return False
        return True

    # Calling destructor
    def __del__(self):
        del self.__temporary_NW_list  # Delete the temporary list to improve the memory management
