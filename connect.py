import subprocess
strx = 'lynx -dump -nolist https://www.vpnbook.com/freevpn > lynx.tmp'
subprocess.call(strx,shell=True)
f_SiteList = open ('lynx.tmp')
lineList = f_SiteList.readlines()
f_SiteList.close()
subprocess.call('rm lynx.tmp',shell=True)
username = ''
password = ''
wordList = list()
x = 0
while x < len(lineList):
    i = 0
    lineWordList = lineList[x].split(' ')
    while i < len(lineWordList):
        wordList.append(lineWordList[i])
        i = i + 1
    x = x + 1
x = 0
while x < len(wordList):
    if wordList[x].lower() == 'username:':
        username = wordList[x + 1]

    if wordList[x].lower() == 'password:':
        password = wordList[x + 1]

    x = x + 1


with open("ovpn.credential", "a") as myfile:
    myfile.write(username)
    myfile.write(password)
myfile.close()

subprocess.call('rm ./*.ovpn',shell=True)
subprocess.call('rm ./VPNBook.com-OpenVPN-Euro1*',shell=True)

subprocess.call('wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-Euro1.zip > /dev/null',shell=True)

subprocess.call('unzip ./VPNBook.com-OpenVPN-Euro1.zip',shell=True)
subprocess.call('nohup sudo openvpn --config vpnbook-euro1-tcp443.ovpn --auth-user-pass ovpn.credential &',shell=True)
subprocess.call('sudo /usr/share/scripts/routerVpnMode-enable',shell=True)
subprocess.call('tail -f nohup.out',shell=True)
