# Initialize 3 empty partitions
p1, p2, p3 = [], [], []

# "Push" data into them
p1.append("User A")
p2.append("User B")
p3.append("User C")

print(f"Part 1: {p1}, Part 2: {p2}, Part 3: {p3}")


def add_user(partition, user):
    """Add a user to the given partition."""
    partition.append(user)


def get_all_users(partitions):
    """Return all users across all partitions."""
    all_users = []
    for partition in partitions:
        all_users.extend(partition)
    return all_users


if __name__ == "__main__":
    add_user(p1, "User D")
    add_user(p2, "User E")

    all_users = get_all_users([p1, p2, p3])
    print(f"All users: {all_users}")
