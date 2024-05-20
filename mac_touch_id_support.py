"""
Code to use touch id verification in python
Github package: https://github.com/lukaskollmer/python-touch-id
Command to install -> pip install git+https://github.com/lukaskollmer/python-touch-id.git

"""
import touchid


def main() -> None:
    print(touchid.is_available())  # to check whether the system has touch id support or not
    is_verified = touchid.authenticate(reason='authenticate via Touch ID')
    # returns true / false based on the fingerprint entered and the fingerprints added in mac
    print(is_verified)


if __name__ == '__main__':
    main()
