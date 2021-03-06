import os
import sys


def get_cmd_args():
    args = sys.argv[1:]
    argsCount = len(args)
    if argsCount == 0:
        return (0, '')
    elif argsCount == 1:
        return (1, args[0])
    else:
        text = args[0]
        for i in range(1, argsCount):
            text += ' '+args[i]
        return (argsCount, text)


if __name__ == '__main__':
    args = get_cmd_args()
    if args[0] != 0:
        if args[1] == 'open':
            os.system("git config --global http.proxy socks5://127.0.0.1:7891")
            os.system("git config --global https.proxy socks5://127.0.0.1:7891")
            print("Open success")
        elif args[1] == 'close':
            os.system("git config --global --unset http.proxy")
            os.system("git config --global --unset https.proxy")
            print("Close success")
        else:
            print("Invalid command")
    else:
        print("Invalid command")
