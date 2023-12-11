from Users_Network import UsersNetwork


class UsersSubnetwork(UsersNetwork):  # Create class UsersSubnetwork which inherits class UsersNetwork
    def __init__(self):
        UsersNetwork.__init__(self)  # Initialising the parent's constructor
        self.__friends_set = set()  # Creating a temporary empty set
        self.__friends_of_friends = []
        self.__user_index = 0

    # Check if user input is valid
    def check_user_index(self):
        self.__user_index = input('Enter a user ID as an integer from 0 to ' + str(self._number_of_users - 1) + ':')
        while self.__user_index == '' or int(self.__user_index) not in range(self._number_of_users):
            self.__user_index = input('User ID does not exist. Try another user ID as an integer from 0 to ' + str(
                self._number_of_users - 1) + ':')
        return self.__user_index

    # Build the subnetwork (for a specific user)
    def __define_user(self):
        self._user_name = list(self._social_NW)[int(self.__user_index)]
        self._user_friends = list(self._social_NW.values())[int(self.__user_index)]

    # Display friends of a user
    def display_friends_of_a_user(self):
        self.__define_user()
        if len(list(self._user_friends)) == 0:
            print('User ' + self._user_name + ' have no friends.')
        else:
            print('User ' + self._user_name + ' have the following friends: ' + ', '.join(list(self._user_friends)))

    # Display number of friends a user have
    def count_number_of_friends(self):
        self.__define_user()
        print('User ' + self._user_name + ' have ' + str(len(self._user_friends)) + ' friends.')

    # Display recommended friends for a user
    def recommend_friends(self):
        self.__define_user()
        for friends in self._user_friends:
            self.__friends_of_friends = self._social_NW[str(friends)]
            for element in self.__friends_of_friends:
                if element not in self._user_friends and element != self._user_name:
                    self.__friends_set.add(element)
        if len(self.__friends_set) == 0:
            print('There are not recommended friends for ' + self._user_name)
        else:
            print('The recommended friend for ' + self._user_name + ' is ' + ', '.join(self.__friends_set))
        self.__friends_set.clear()  # Clear the set

    # Display friends of a user's friends
    def friends_of_the_friends(self):
        self.__define_user()
        if len(self._user_friends) == 0:
            print('User ' + self._user_name + ' have no friends.')
        else:
            for friend in self._user_friends:
                self.__friends_of_friends = self._social_NW[str(friend)]
                for element in self.__friends_of_friends:
                    if element != self._user_name:
                        self.__friends_set.add(element)
                if len(self.__friends_set) == 0:
                    print(str(friend) + ' -> none')
                else:
                    print(str(friend) + ' -> ' + ', '.join(self.__friends_set))
                self.__friends_set.clear()  # Clear the set

    # Calling the destructor
    def __del__(self):
        del self.__friends_set  # Delete the temporary set
