import os, sys

def main():
    try:
        version = "0.3.1"
        if len(sys.argv) > 1 and sys.argv[1] in ['-v', '--version', '-V']:
            print(f"uDFC v{version}")
            sys.exit(0)

        Entry = {}
        # essential stuff
        Entry['Name'] = input("Enter the program name: ")
        Entry['Exec'] = input("Enter the program path: ")
        Entry['Comment'] = input("Enter a comment: ")
        Entry['Workdir'] = input("Enter the working directory (leave empty if unknown): ")
        Entry['Version'] = input("Enter the program's version: ")
        # ask if program should be ran in a terminal
        while True:
            Entry['Terminal'] = input("Do you want to open the program in a terminal? [Y/n] ")
            if Entry['Terminal'] in ['n', 'N']:
                Entry['Terminal'] = False
                break
            elif Entry['Terminal'] in ['y', 'Y']:
                Entry['Terminal'] = True
                break
            else:
                print("Invalid response")
                continue
        # ask for the program type
        print("Available program types:")
        types = ['Link', 'Application', 'Directory']
        for i in types:
            print(i)
        while True:
            Entry['Type'] = input("Enter one of the listed Types: ")
            if Entry['Type'] not in types:
                continue
            else:
                break
        while True:
            # ask where to write the output
            WillInstall = input("Do you want to install the file? [Y/n] ")
            if WillInstall in ['Y', 'y']:
                os.makedirs(f'{os.path.expanduser('~')}/.local/share/applications', exist_ok=True)
                with open(f'{os.path.expanduser('~')}/.local/share/applications/{Entry['Name']}.desktop', 'w') as entry:
                    entry.write('[Desktop Entry]\n')
                    entry.write(f'Type={Entry['Type']}\n')
                    entry.write(f"Version={Entry['Version']}\n")
                    entry.write(f"Name={Entry['Name']}\n")
                    entry.write(f"Path={Entry['Workdir']}\n")
                    entry.write(f"Exec={Entry['Exec']}\n")
                    entry.write(f"Terminal={Entry['Terminal']}\n")
                break
            elif WillInstall in ['N', 'n']:
                    print('[Desktop Entry] ')
                    print(f'Type={Entry['Type']} ')
                    print(f"Version={Entry['Version']} ")
                    print(f"Name={Entry['Name']} ")
                    print(f"Path={Entry['Workdir']} ")
                    print(f"Exec={Entry['Exec']} ")
                    print(f"Terminal={Entry['Terminal']} ")
                    break
            else:
                continue
    except Exception as e:
        print(f"Error: {e}")
        return e
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        raise e