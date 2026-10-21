robots = []


def add_robot(name):
    robots.append(name)
    print(f"{name} added successfully.")


def show_robots():
    print("\nRegistered Robots:")

    for robot in robots:
        print(f"- {robot}")


add_robot("Atlas")
add_robot("Spot")

show_robots()
