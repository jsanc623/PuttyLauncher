import ConfigParser
from Tkinter import *
from subprocess import call


def main():
    master = Tk()

    config = load_config()
    set_window(master)
    set_buttons(master, config['servers'], config)

    master.pack_propagate(0)
    master.mainloop()


def load_config():
    config = ConfigParser.SafeConfigParser()
    config.read("config.ini")
    return {'private-key': config.get('private-key', 'location'),
            'servers': config.get('servers', 'servers').split("\n"),
            'username': config.get('user', 'username'),
            'putty-location': config.get('putty', 'location')
            }


def set_window(master):
    master.geometry("640x600")
    master.wm_title("Putty Launcher")
    master.iconbitmap(default='icon.ico')


def set_buttons(master, config, global_config, row=0, column=0):
    for single_button_data in config:
        button_data = single_button_data.split("::")
        Button(master, width=20, height=4, font=('Courier New', 10), text=button_data[0],
               command=lambda m=button_data[0], n=button_data[1], q=global_config: open_putty(m, n, q)) \
            .grid(row=row, column=column, padx=20, pady=10)

        if column >= 2:
            row += 1
            column = 0
        else:
            column += 1


def open_putty(name, address, config):
    call(config['putty-location'] + " -ssh " + config['username'] + "@" + address + " -i " + config[
        'private-key'] + " -v")


if __name__ == '__main__':
    main()
