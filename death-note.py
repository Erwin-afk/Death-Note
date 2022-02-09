import os, time, sys, socket
from re import S
from colorama import Fore, Style
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
init()

name = socket.gethostname()


def intro():
    title=(f"""\n{Fore.LIGHTWHITE_EX}𝕯 𝖊 𝖆 𝖙 𝖍  𝕹 𝖔 𝖙 𝖊{Style.RESET_ALL}""")
    print(title)
    print(f"{Fore.LIGHTBLACK_EX}𝖒𝖆𝖉𝖊 𝖇𝖞 𝖊𝖗𝖜𝖎𝖓{Style.RESET_ALL}\n")
intro()


def main():
    person = input(f"{Fore.RED}𝔫𝔞𝔪𝔢{Style.RESET_ALL}")
    reason = input(f"{Fore.RED}𝔯𝔢𝔞𝔰𝔬𝔫{Style.RESET_ALL}")
    os.system("cls")

    if person == "":
        person = name

    elif person == "creator":
        person = "Erwin Ny."

    elif person == "chonker":
        person = f"{Fore.LIGHTYELLOW_EX}CHONKER{Style.RESET_ALL}"
    
    if reason == "":
        reason = "heart attack"

    text = (f"{Fore.LIGHTRED_EX}Ryuk{Style.RESET_ALL}: {person} died due {reason}.\n")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    intro()
    main()

main()

#Made by Erwin.