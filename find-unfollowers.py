# To find the followers that do not reciprocate followship for a particular user, run this script with USERNAME arg in this format:
# python3 find_unfollowers.py USERNAME
# e.g. >> python3 find_unfollowers arianagrande
from bot import find_unfollowers
import sys

if __name__ == "__main__":

    account = sys.argv[1]
    find_unfollowers(account)

    
        
        