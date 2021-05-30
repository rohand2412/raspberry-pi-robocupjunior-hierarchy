import subprocess

def main():
    """Main code"""
    for i in range(3):
        while True:
            if not check_for_reset("python3 /home/pi/Documents/PyFiles/raspberry-pi-robocupjunior-line/main.py --mode silver"):
                if not check_for_reset("python3 /home/pi/Documents/PyFiles/raspberry-pi-robocupjunior-evac/main.py"):
                    if not check_for_reset("python3 /home/pi/Documents/PyFiles/raspberry-pi-robocupjunior-line/main.py --mode red"):
                        break

def check_for_reset(command):
    """Checks printout of command for reset flag"""
    verbose = subprocess.check_output(command, shell=True)

    verbose = verbose.decode()
    print(verbose)

    lines = verbose.split("\n")
    if lines[-2] == "RESET":
        return True
    return False

if __name__ == '__main__':
    main()
