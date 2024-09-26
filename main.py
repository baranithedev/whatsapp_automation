import setup
import banner_config

def display_menu():
    banner_config.final_banner()


def start_main_script():
    display_menu()
    option=str(input("Enter The Option: >> "))
    whatsappMessageAutomation = setup.WhatappMessageAutomation(option.lower())
    whatsappMessageAutomation.user_choice()
