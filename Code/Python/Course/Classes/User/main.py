from admin import User, Admin

harry = User('harry', 'taylor', 16, 'male')
matteo = User('matteo', 'degaye', 17, 'male')
aymeric = User('aymeric', 'deloor', 17, 'male')



ron = Admin('ron', 'jaques', '32', 'male')

ron.show_privileges()
