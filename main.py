import subprocess

def main():
    """Main code"""
    while True:
        if not check_for_reset("python3 spammer-1.py"):
            if not check_for_reset("python3 spammer-2.py"):
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
