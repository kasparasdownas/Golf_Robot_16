from robot_control import *
from vision import detect_balls
import vision

#bare en test
def main():
    print("Starting GolfBot...")
    move_forward()
    balls = detect_balls()
    print(f"Detected {len(balls)} balls.")

if __name__ == "__main__":
    main()
