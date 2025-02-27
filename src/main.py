from robot_control import move_forward
from vision import detect_balls
import vision
import robot_control

#bare en test
def main():
    print("Starting GolfBot...")
    move_forward()
    balls = detect_balls()
    print(f"Detected {len(balls)} balls.")

if __name__ == "__main__":
    main()
