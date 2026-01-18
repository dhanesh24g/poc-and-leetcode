from dbms.userdata_management import UserDataManagement

class User:
    pass

if __name__ == '__main__':

    option = input("Choose operation (1:Insert Data / 2:Retrieve Data): ")

    userdata = UserDataManagement()
    user = User()

    if option == "1":
        user.name = input("Enter name: ")
        user.surname = input("Enter surname: ")
        user.age = input("Enter age: ")

        userdata.insert_user_data(user)

    if option == "2":
        user.id = input("Enter UserID to Retrieve: ")

        userdata.get_user_data(user.id)