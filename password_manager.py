import random
import string
import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def hash_password(self, password):
        # Use a strong hashing algorithm like SHA-256 for better security
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        password_hash = binascii.hexlify(password_hash)
        return (salt + password_hash).decode('ascii')

    def add_password(self, website, username, password):
        password_hash = self.hash_password(password)
        self.passwords[website] = {'username': username, 'password': password_hash}
        print(f"Password for '{website}' added successfully!")

    def get_password(self, website):
        if website in self.passwords:
            return self.passwords[website]['password']
        else:
            print(f"Password for '{website}' not found.")

def main():
    password_manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Generate and Add Password")
        print("2. Get Password")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            website = input("Enter the website or service name: ")
            username = input("Enter the username: ")
            password = password_manager.generate_password()
            print(f"Generated Password: {password}")
            password_manager.add_password(website, username, password)
        elif choice == '2':
            website = input("Enter the website or service name: ")
            password = password_manager.get_password(website)
            if password:
                print(f"Password for '{website}': {password}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
