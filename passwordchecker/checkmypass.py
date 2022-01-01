import requests
import hashlib      #allows us to calc SHA1 hashes
import sys

#Request from site all the hashs that match our sub query characters
def request_api_data(part_hash):
    url = 'http://api.pwnedpasswords.com/range/' + part_hash
    res = requests.get(url)     #contains 100's of hashed passwords we need to check
    if res.status_code != 200:  #display if we get an error
        raise RuntimeError(f'Error fetching: {res.status_code}, check API again')
        print(res.status_code)
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    print(f'Hash to check is: {hash_to_check}')
    print()
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

#Once we have hashes we want to check our password again this
def pwned_api_check(password):
    hash = hashlib.sha1(password.encode('utf8')).hexdigest().upper()
    print(f'Which hashing into {hash[:5]} and {hash[5:]}')
    first5, tail = hash[:5], hash[5:]
    print()
    response = request_api_data(first5)
    
    return get_password_leaks_count(response, tail)


def main(args):
    pwd_to_check = args
    print(f'Lets see is any of these passwords have been pwned: {pwd_to_check}')
    print()
    for pwd in pwd_to_check:
        print(f'Checking password: {pwd}')
        count = pwned_api_check(pwd)
        if count:
            print(f'Holy crap!! {pwd} has been pwned a total of {count} times, maybe you should change it!')

        else:
            print(f'Nice job!! {pwd} was found to be pwned a total of {count} times, carry on!')
if __name__ == '__main__':
   
   main(sys.argv[1:])