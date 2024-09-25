robot_location = 25
ball_location = 30
goal_location = 15
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False
    
#1 I think that if the if function is satisfied it will do what's under it
#2 A code is enclosed in a branch if the code had a line infront of it and has the if funtion above it. For example, all the print funcitons in this code are under an if funciton because there is an if funtion over them and the're is a line in fornt of them.
#4 += adds an amount to a variable and -= subtracts an amount from a variable