#Simulate user request.
# 1. Single requests from single user
# 2. Parallel requests from 3 users.
import threading
from src.Users.userActions import Users
from src.Location.locationService import Location

if __name__ == "__main__":
    user1Location = Location("POINT",10.12,10.15)
    user1 = Users("user1",user1Location)
    user2 = Users("user2",user1Location)
    user3 = Users("user3",user1Location)

    user1.requestTaxi()

    # creating thread
    t1 = threading.Thread(target=user2.requestTaxi(), args=())
    t2 = threading.Thread(target=user3.requestTaxi(), args=())

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")