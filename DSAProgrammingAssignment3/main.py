inputA = ["2\n", "1 1 4\n", "7 3 5\n"]  # simulating hackerrank input()

lines = inputA

number_of_boundaries = lines[0]  # can be used in a loop

start_x_coordinates = []
end_x_coordinates = []
y_coordinate_end_barriers = []

for i in lines:
    i.strip()  # removes the newline character
    if i != lines[0]:
        a, b, c = i.split()
        x_boundary_start = int(a)
        x_boundary_stop = int(a) + int(c)
        start_x_coordinates.append(x_boundary_start)
        end_x_coordinates.append(x_boundary_stop)
        y_coordinate_end_barriers.append(int(b))

# print(start_x_coordinates)
# print(end_x_coordinates)

blocked_ants = []

for i in range(len(start_x_coordinates)):
    number_of_ants = abs(start_x_coordinates[i] - end_x_coordinates[i]) + 1
    blocked_ants.append(number_of_ants)


# print(blocked_ants)
print(sum(blocked_ants))
