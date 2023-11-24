# Python RPG
# Elias Tagariello
import sys
import functions
import colors


def start_game():
    # greetings and initial
    hello_first_name = "Hello there! What's you're first name?\n"
    functions.type_out_prompt(hello_first_name)
    first_name = input("> ")
    functions.if_quit(first_name)

    while True:
        # if given first name
        if first_name.find(' ') == -1:  # this checks if they only said their first name
            last_name_question = f"And what's your last name, {first_name}?\n"
            functions.type_out_prompt(last_name_question)

            didnt_hear_last_name = input("> ")  # when given last name
            functions.if_quit(didnt_hear_last_name)

            last_name_confusion = "Huh? Can you repeat that?\n"
            functions.type_out_prompt(last_name_confusion)

            last_name = input("> ")
            functions.if_quit(last_name)

            # to see if they changed their last name
            if last_name.lower() != didnt_hear_last_name.lower():
                you_lying = (f"No, that's not what you said before, you lying b****. "
                             f"{colors.colors.RED}{colors.colors.BOLD}don't lie...{colors.colors.RESET}\n")
                functions.type_out_prompt(you_lying)

                last_name = input("> ")
                functions.if_quit(last_name)

                if last_name.lower() != didnt_hear_last_name.lower():
                    nah_im_done = f"Nah, I'm not about to deal with this pri**. Cya."
                    functions.type_out_prompt(nah_im_done)
                    sys.exit()

                else:
                    you_better_have = "Yeah that's what I thought...\n"
                    functions.type_out_prompt(you_better_have)
            # inner if statement end

            # back to talking about their last name
            last_name_disgust = (f"Wait... {last_name}... That's your last name?... "  # bully last name
                                 f"How unfortunately hideous... I almost pity you... "
                                 f"Please don't mention it ever again.\n")
            functions.type_out_prompt(last_name_disgust)
            break
            # this break is so that it doesn't also mention the else

        else:
            # if given a last name with first in same response
            given_first_and_last = (f"I only asked for your first name, bozo. "
                                    f"If you can't follow simple rules, skedaddle.")
            functions.type_out_prompt(given_first_and_last)
            sys.exit()
        # outer if statement end
    # while loop ended

    # back to questioning
    how_are_you = f"Anyways... If there was one word to describe how you feel right now, what would it be, {first_name}?\n"
    functions.type_out_prompt(how_are_you)
    feelings = input("> ")
    functions.if_quit(feelings)
    functions.if_lastname_ever_mentioned_again(last_name, feelings)

    what = "What?\n"
    functions.type_out_prompt(what)
    repeated_feelings = input("> ")
    functions.if_quit(repeated_feelings)
    functions.if_lastname_ever_mentioned_again(last_name, repeated_feelings)

    idc = "Oh, sorry. I forgot to care... So lets begin!\n"
    functions.type_out_prompt(idc)

    # begin survey

