import pywhatkit as pwk 
import pyautogui as pg
from banner_config import terminal_size
#import time
import csv

class WhatappMessageAutomation():
    def __init__(self, option):
        self.option = option

    def start_bombing(self, message_text_file: str, process_count: int, delay: int):
        print(f"Note: Attack Will Started With {delay}\'s Delay!.")
        for _ in range(process_count):
            pass
            pg.write(open(message_text_file, 'rb').read().decode())
            pg.press("Enter")
        print("Process Completed!...")

    def send_messages_bulk_contacts(self, message_count: int, contacts_fp: str, sth: int, stm: int, delay: int):
        messages=[]
        for _ in range(message_count):
            message = str(input("Enter your message: "))
            messages.append(message)

        with open(contacts_fp, 'r') as file:
            contacts = csv.reader(file)
            for contact in contacts:
                for message in messages:
                    pwk.sendwhatmsg(contact[1], message, sth, stm, delay, True)
                    print("{} - {} Send Message Sucessfully!.".format(contact[0], contact[1]))
            print("Process Completed!...")

    def search_user_with_number(self, number, contacts_fp):
        with open(contacts_fp, 'r') as file:
                    exist_contacts=csv.reader(file)
                    for exist_contact in exist_contacts:
                        if exist_contact[1] == number:
                            print('User exists')
                            break
                    else:
                        print("User doesn't exists!.")
                        add_or_not= input("Do you want add this number! (y/n): ")
                        contacts_fp=input("Enter contacts file path: ")
                        match add_or_not.lower():
                            case 'y':
                                new_user_name=input("Enter this number {} user name: ".format(number))
                                with open(contacts_fp, 'w+', newline='') as file:
                                    write_file = csv.writer(file)
                                    write_file.writerow([str(new_user_name), (number)])


    def user_choice(self):
        match self.option:
            case '1':
                umc=int(input("How many messages you want to send: "))
                cfp=str(input("Enter contacts file path: "))
                sth=int(input("Hours in railway time format: "))
                stm=int(input("Minutes: "))
                dly=int(input("Delay: "))
                self.send_messages_bulk_contacts(umc, cfp, sth, stm, dly)

            case '2':
                fl=str(input("Enter file path: "))
                pc=int(input("How much messages: "))
                dl=int(input("Delay Seconds: "))
                self.start_bombing(fl, pc, dl)

            case '3':
                user_number=str(input("Enter Mobile Number To Search: "))
                contacts_fp=str(input("Enter contacts file path: ")) 
                self.search_user_with_number(user_number, contacts_fp)

            case '5':
                print('Program Exitted. Thankyou!.'.center(terminal_size))

            case 'h':
                print("Comming soon!")

            case _:
                print("Quitting!. You Don't Have An Enter A Valid Option!.".center(terminal_size))
                print("Thankyou!...".center(terminal_size))

