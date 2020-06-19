class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    else:
        for g in group.groups:
            return is_user_in_group(user,g)
    return False

#testing case
#Groups
parent = Group("parent")

child1 = Group("child1")
child2 = Group("child2")

sub_child11 = Group("subchild11")
sub_child12 = Group("subchild12")

sub_child21 = Group("subchild21")
sub_child22 = Group("subchild22")

#Users
parent_user_1 = "parent_user_1"
child1_user_1 = "child1_user_1"
child2_user_1 = "child2_user_1"
sub_child11_user_1 = "sub_child11_user_1"
sub_child12_user_1 = "sub_child12_user_1"
sub_child21_user_1 = "sub_child21_user_1"
sub_child22_user_1 = "sub_child22_user_1"

parent_user_2 = "parent_user_2"
child1_user_2 = "child1_user_2"
child2_user_2 = "child2_user_2"
sub_child11_user_2 = "sub_child11_user_2"
sub_child12_user_2 = "sub_child12_user_2"
sub_child21_user_2 = "sub_child21_user_2"
sub_child22_user_2 = "sub_child22_user_2"

parent.add_user(parent_user_1)
parent.add_user(parent_user_2)

parent.add_group(child1)
child1.add_user(child1_user_1)
child1.add_user(child1_user_2)

parent.add_group(child2)
child2.add_user(child2_user_1)
child2.add_user(child2_user_2)

child1.add_group(sub_child11)
sub_child11.add_user(sub_child11_user_1)
sub_child11.add_user(sub_child11_user_2)

child1.add_group(sub_child12)
sub_child12.add_user(sub_child12_user_1)
sub_child12.add_user(sub_child12_user_2)

child2.add_group(sub_child21)
sub_child21.add_user(sub_child21_user_1)
sub_child21.add_user(sub_child21_user_2)

child2.add_group(sub_child22)
sub_child22.add_user(sub_child22_user_1)
sub_child22.add_user(sub_child22_user_2)


# Parent1 in Parent
print ("Pass" if (is_user_in_group(parent_user_1, parent) == True) else "Fail")

# Parent2 in Parent
print ("Pass" if (is_user_in_group(parent_user_2, parent) == True) else "Fail")

# Child1_1 in Parent
print ("Pass" if (is_user_in_group(child1_user_1, parent) == True) else "Fail")

# Child1_2 in Parent
print ("Pass" if (is_user_in_group(child1_user_2, parent) == True) else "Fail")

# SubChild11_2 in Parent
print ("Pass" if (is_user_in_group(sub_child11_user_2, parent) == True) else "Fail")

# Subchild22_2 in Child1
print ("Pass" if (is_user_in_group(sub_child22_user_2, child1) == False) else "Fail")

# Subchild11_1 in Child2
print ("Pass" if (is_user_in_group(sub_child11_user_1, child2) == False) else "Fail")

# Non exist user
print ("Pass" if (is_user_in_group('sub_child11_user_random', child2) == False) else "Fail")

# Null user
print ("Pass" if (is_user_in_group('', child1) == False) else "Fail")
