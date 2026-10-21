robots = []


def add_robot(name):
    robots.append(name)
    print(f"{name} added successfully.")


def show_robots():
    print("\nRegistered Robots:")

    for robot in robots:
        print(f"- {robot}")


def assign_task(robot, task):
    print(f"{robot} assigned task: {task}")


add_robot("Atlas")
add_robot("Spot")

show_robots()

assign_task("Atlas", "Inspect warehouse")