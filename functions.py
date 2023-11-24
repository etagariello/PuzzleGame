import sys
import time
import colors


def if_quit(text):
    if text.lower() == ("quit"):
        sys.exit()


def type_out_prompt(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust the delay time (in seconds) for typing speed


def type_out_extra_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.5)  # Adjust the delay time (in seconds) for typing speed


last_name_counter = 0


def if_lastname_ever_mentioned_again(last_name, maybe_last_name):
    if last_name == maybe_last_name:
        warning1 = (f"Hey man, I've done told you not to tell me your ugly a** last name. Do it again, "
                    f"{colors.colors.BOLD}{colors.colors.RED}AND THERE WILL BE CONSEQUENCES.{colors.colors.RESET}\n")
        type_out_prompt(warning1)
        continue1 = input("> ")
        if_quit(continue1)

        if last_name == continue1:
            warning2 = f"{colors.colors.RED}you did this...{colors.colors.RESET}\n"
            type_out_extra_slow(warning2)
            sys.exit()

        else:
            print("Yeah, that's what I thought")
