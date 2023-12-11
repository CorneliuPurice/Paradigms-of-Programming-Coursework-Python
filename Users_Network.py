from File_Handling import FileHandling


class UsersNetwork(FileHandling):  # Create class UsersNetwork which inherits class FileHandling

    def __init__(self):
        FileHandling.__init__(self)  # Initialising the parent's constructor
        self._user_name = ''
        self._user_friends = ''
        self._number_of_friends = {}
        self._network_display = []
        self.min_value = 0
        self.__common_friends = []
        self.__temp_counter_list = []

    # Build the network
    def __define_network(self):
        self.__common_friends.clear()
        for user in range(self._number_of_users):
            self._user_name = list(self._social_NW)[user]
            self._user_friends = ', '.join(list(self._social_NW.values())[user])
            for sub_user in range(self._number_of_users):
                counter = 0
                sub_user_friends = list(self._social_NW.values())[sub_user]
                for sub_friend in list(self._social_NW.values())[user]:
                    if sub_friend in sub_user_friends:
                        counter += 1
                self.__temp_counter_list.append(str(counter))
            self.__common_friends.append(self._user_name + ' -> ' + ', '.join(list(self.__temp_counter_list)))
            self.__temp_counter_list.clear()
            self._network_display.append(self._user_name + ' -> ' + self._user_friends)
            self._number_of_friends[self._user_name] = len(list(self._social_NW.values())[user])

    # Display the network
    def display_network(self):
        self.__define_network()
        for element in self._network_display:
            print(element)

    # Display common friends
    def display_common_friends(self):
        self.__define_network()
        for element in self.__common_friends:
            print(element)

    # Establish which user have no friends or have the least friends
    def least_friends(self):
        self.__define_network()
        self.min_value = min(self._number_of_friends.values())
        if self.min_value == 0:
            keys = [k for k, v in self._number_of_friends.items() if v == self.min_value]
            print('The user with 0 friends is: ' + ', '.join(keys))
            for j in keys:
                self._number_of_friends.pop(j)
            self.min_value = min(self._number_of_friends.values())
            keys = [k for k, v in self._number_of_friends.items() if v == self.min_value]
            print('The user with least friends is: ' + ', '.join(keys))
        else:
            keys = [k for k, v in self._number_of_friends.items() if v == self.min_value]
            print('The user with least friends is: ' + ', '.join(keys))
