import os
import datetime
terminal_size=os.get_terminal_size().columns

BANNER="Whatsapp Automation v1.0 - Barani Dharan"
MEDIAS="INSTAGRAM:>> _barani_.k._ | GITHUB:>> baranithedev"
YEAR="Since {}".format(datetime.date.today().year)
MENU_OPTION ="""1) Send Bulk Messages \t2) Message Bombing
3) Search Number \t4) Add Number 
5) Exit Program \tH - Help"""

#REUSABLE FUNCTIONS
def final_banner():
    print(BANNER.center(terminal_size))
    print(MEDIAS.center(terminal_size))
    print(YEAR.center(terminal_size))
    print(generate_lines('-'))
    print(MENU_OPTION)
    print(generate_lines('-'))

def generate_lines(charac: str):
    return charac*os.get_terminal_size().columns
