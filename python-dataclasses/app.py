from user import User

u = User('bob', 'password')
u2 = User('bob', 'password')

print(u)

print(u == u2)