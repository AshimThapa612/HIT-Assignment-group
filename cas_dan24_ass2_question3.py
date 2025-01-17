# eg
# 
# 
#  Enter the left branch angle: 30
# Enter the right branch angle: 25
# Enter the starting branch length: 100
# Enter the recursion depth: 6
# Enter the branch length reduction factor (e.g., 0.7 for 70%): 0.7
# Tree drawing saved as 'tree_pattern.eps'.



import turtle

def draw_branch(branch_length, angle, depth, reduction_factor):
    if depth == 0:
        return
    else:
        # Draw the current branch (starting branch) with brown color
        if depth == 1:
            turtle.color("green")  # Change to green for leaves (top of the tree)
        else:
            turtle.color("brown")  # Brown color for branches

        turtle.pensize(depth)  # Optional: Change pen size based on depth
        turtle.forward(branch_length)
        
        # Draw the right branch
        turtle.right(angle)
        draw_branch(branch_length * reduction_factor, angle, depth - 1, reduction_factor)
        
        # Draw the left branch
        turtle.left(angle * 2)  # Turn left by double the angle
        draw_branch(branch_length * reduction_factor, angle, depth - 1, reduction_factor)
        
        # Return to the original position and orientation
        turtle.right(angle)  # Turn back to the right
        turtle.backward(branch_length)  # Go back to the previous position

def main():
    # Get user input
    left_angle = float(input("Enter the left branch angle (in degrees): "))
    right_angle = float(input("Enter the right branch angle (in degrees): "))
    branch_length = float(input("Enter the starting branch length: "))
    depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

    # Set up the turtle
    turtle.speed(0)  # Fastest drawing speed
    turtle.left(90)  # Start facing upwards
    turtle.up()  # Lift the pen
    turtle.backward(100)  # Move back to start position
    turtle.down()  # Put the pen down

    # Draw the tree
    draw_branch(branch_length, right_angle, depth, reduction_factor)

    # Finish up
    turtle.done()

if __name__ == "__main__":
    main()
