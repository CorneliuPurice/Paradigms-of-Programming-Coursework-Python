"""
STUDENT - Purice Corneliu
COMP1811 COURSEWORK
"""
from Users_Subnetwork import UsersSubnetwork

while True:  # Run the program until the user didn't break the loop
    network = UsersSubnetwork()  # Creating the object
    fileInput = input('Enter a filename for network data:')  # User input the file name
    if fileInput in ('n', 'N'):
        break
    if not network.check_file_name(fileInput):
        break
    network.read_data_from_file()
    network.assign_keys()
    network.assign_values()

    if not network.check_consistency():  # Check if the network is inconsistent
        if input('Display the social network (y/n)?') in ('y', 'Y'):
            network.display_network()
    else:  # If the network is consistent, give user the following options
        if input('Display the social network (y/n)?') in ('y', 'Y'):
            network.display_network()

        if input('Display common friends (y/n)?') in ('y', 'Y'):
            network.display_common_friends()

        if input('Display friends of a user (y/n)?') in ('y', 'Y'):
            network.check_user_index()
            network.display_friends_of_a_user()

        if input('Recommend friends for a user (y/n)?') in ('y', 'Y'):
            network.check_user_index()
            network.recommend_friends()

            while input('Do you want to recommend friends to another user (y/n)?') in ('y', 'Y'):
                network.check_user_index()
                network.recommend_friends()

        if input('Display how many friends a user has (y/n)?') in ('y', 'Y'):
            network.check_user_index()
            network.count_number_of_friends()

        if input('Display the users with the least number of or have 0 friends (y/n)?') in ('y', 'Y'):
            network.least_friends()

        if input('Display the friends of the friends of a given user (y/n)?') in ('y', 'Y'):
            network.check_user_index()
            network.friends_of_the_friends()

    if input('Do you want to try another social network (y/n)?') in ('y', 'Y'):
        continue  # This will run the loop again
    else:
        break  # This will break the loop
