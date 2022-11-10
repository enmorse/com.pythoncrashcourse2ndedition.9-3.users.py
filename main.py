class User:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f'The user\'s name is {self.last_name}, '
              f'{self.first_name} and their email address is '
              f'{self.email}.')

    def greet_user(self):
        print(f'\nHello, {self.first_name} {self.last_name} '
              f'your email address is {self.email}, is that '
              f'correct?')


def main():
    user_one = User('Ernest', 'Morse', 'enmorse48@gmail.com')
    user_two = User('Marcus', 'Aurelius', 'marcusaurelius@email.com')
    user_three = User('Albert', 'Einstein', 'alberteinstein@email.com')

    user_one.describe_user()
    user_one.greet_user()

    user_two.describe_user()
    user_two.greet_user()

    user_three.describe_user()
    user_three.greet_user()


if __name__ == '__main__':
    main()
