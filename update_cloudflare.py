import requests
import easyufw as ufw

cloudflare_ips = requests.get('https://www.cloudflare.com/ips-v4').text.split('\n')


def update_cloudflare():
    for ip in cloudflare_ips:
        if ip != '':
            print('Allowing %s' % ip)
            ufw.run('allow from %s' % ip)


print('Reseting ufw...')
ufw.reset()
print('Adding OpenSSH...')
ufw.allow('OpenSSH')
print('Adding Cloudflare IPs to the whitelist...')
update_cloudflare()
print('Enabling ufw...')
ufw.enable()
print('Everything is done!')
