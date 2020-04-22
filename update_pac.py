# coding=utf-8
# Copyright (c) 2020. Xinyi Chen
import re
import keyboard
import pyautogui as pag
import pyperclip
import os

path_pac = r'pac.txt'  # path of pac.txt
delim_line = '--------------------------------------------------------------------------------------------------------------------------------------------------------------'


def reboot_server_process():
    os.system('taskkill /f /im v2rayN.exe')
    os.system('start v2rayN.exe')
    print('v2rayN service restarted.')


def print_banner():
    print('\n')
    print(
        '          .d8888b.                            888b    888       8888888b.      d8888  .d8888b.                      888      888                  \n'
        '         d88P  Y88b                           8888b   888       888   Y88b    d88888 d88P  Y88b                     888      888                  \n'
        '                888                           88888b  888       888    888   d88P888 888    888                     888      888                  \n'
        '888  888      .d88P 888d888  8888b.  888  888 888Y88b 888       888   d88P  d88P 888 888               8888b.   .d88888  .d88888  .d88b.  888d888 \n'
        '888  888  .od888P"  888P"       "88b 888  888 888 Y88b888       8888888P"  d88P  888 888                  "88b d88" 888 d88" 888 d8P  Y8b 888P"   \n'
        'Y88  88P d88P"      888     .d888888 888  888 888  Y88888       888       d88P   888 888    888       .d888888 888  888 888  888 88888888 888     \n'
        ' Y8bd8P  888"       888     888  888 Y88b 888 888   Y8888       888      d8888888888 Y88b  d88P       888  888 Y88b 888 Y88b 888 Y8b.     888     \n'
        '  Y88P   888888888  888     "Y888888  "Y88888 888    Y888       888     d88P     888  "Y8888P"        "Y888888  "Y88888  "Y88888  "Y8888  888     \n'
        '                                          888                                                                                                     \n'
        '                                     Y8b d88P                                                                                                     \n'
        '                                      "Y88P"                                                                                                      \n'
        '\nCopyright (c) 2020. Xinyi Chen | https://github.com/Hyperkopite/v2rayN-pac-adder')
    print(delim_line + '\n[*]Add: ctrl + shift + insert\n[*]Delete: ctrl + shift + del\n\nWaiting for your command...')
    pag.keyDown('alt')
    pag.keyDown('space')
    pag.press('x')
    pag.keyUp('alt')
    pag.keyUp('space')


def add_to_pac():
    domain = parse_url()
    if domain == '':
        print(
            delim_line + '\n[*]Add: ctrl + shift + insert\n[*]Delete: ctrl + shift + del\n\nWaiting for your command...')
        return
    cntr_line = 0
    is_exist = False
    with open(path_pac, 'r+', encoding='utf-8') as f_pac:
        lines = f_pac.readlines()
        f_pac.seek(0, 0)
        f_pac.truncate()
        for line in lines:
            if line == '  \"' + domain + '\",\n':
                is_exist = True
                break
        if not is_exist:
            for line in lines:
                if line == 'var rules = [\n':
                    line += '  \"' + domain + '\",\n'
                    lines[cntr_line] = line
                    break
                cntr_line += 1
        f_pac.writelines(lines)
    if is_exist:
        print('\nDomain [' + domain + '] already exists!')
    else:
        print('\n[' + domain + '] added to PAC list\n')
        reboot_server_process()
    print(delim_line + '\n[*]Add: ctrl + shift + insert\n[*]Delete: ctrl + shift + del\n\nWaiting for your command...')


def del_from_pac():
    domain = parse_url()
    cntr_line = 0
    is_exist = False
    if domain == '':
        print(
            delim_line + '\n[*]Add: ctrl + shift + insert\n[*]Delete: ctrl + shift + del\n\nWaiting for your command...')
        return
    with open(path_pac, 'r+', encoding='utf-8') as f_pac:
        lines = f_pac.readlines()
        f_pac.seek(0, 0)
        f_pac.truncate()
        for line in lines:
            match = re.search(re.compile(r'".*"(?=,?\n)'), line)
            # print(line, domain)
            if match is not None:
                match = match.group().strip('\"')
                if match != '|' and (match.find(domain) != -1 or match == domain):
                    lines[cntr_line] = ''
                    print('\nDomain [' + match + '] has been removed successfully!')
                    is_exist = True
            cntr_line += 1
        f_pac.writelines(lines)
    if is_exist:
        reboot_server_process()
    else:
        print('\n[' + domain + '] doesn\'t exist!')
    print(
        delim_line + '\n[*]Add: ctrl + shift + insert\n[*]Delete: ctrl + shift + del\n\nWaiting for your command...')


def parse_url():
    no_dot = False
    url = str(pyperclip.paste())
    print('URL: ' + url)
    url_cut = re.search(re.compile(r'//[\w.-:]+/'), url)
    if url_cut is not None:
        url = url_cut.group()
    domain = re.search(re.compile(r'((?<=\.)([\w-]+\.){1,2}\w+(?=/|$|:))'), url)
    if domain is None:
        domain = re.search(re.compile(r'(?<=//)([\w-]+\.){1,2}\w+(?=/|$|:)'), url)
        if domain is None:
            print('Failed to parse the URL, wanna manually input? [Y(y) / N(n)]')
            if 'Yy'.find(input()) != -1:
                url = input('\nURL: ')
            else:
                return ''
        else:
            no_dot = True
    domain = domain.group() if no_dot is True else url if domain is None else '.' + domain.group()
    return domain


def go():
    try:
        keyboard.add_hotkey('ctrl + shift + insert', add_to_pac)
        keyboard.add_hotkey('ctrl + shift + delete', del_from_pac)
    except Exception as e:
        print(e)
        keyboard.remove_hotkey('ctrl + shift + insert')
        keyboard.remove_hotkey('ctrl + shift + delete')
        print(
            delim_line + '\n[*]Add: ctrl + shift + insert\n[*]Delete: ctrl + shift + del\n\nWaiting for your command...')
        return go()
    while 1:
        pass


if __name__ == '__main__':
    print_banner()
    go()
