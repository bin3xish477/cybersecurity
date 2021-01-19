# File Canary

Get an email whenever a file you intentionally create to lure attackers gets opened. This should be installed as a cronjob (Linux) or scheduled task (Windows). Enjoy!

### Usage

Set the following environment variables:

- `EMAIL_ADDR` - gmail address
- `EMAIL_PASS` - gmail password (if you are using 2fa authentication, you need to create an app password to authenticate to gmail

Getting an app password: [app_password](https://www.lifewire.com/get-a-password-to-access-gmail-by-pop-imap-2-1171882)
	
```
usage: canary.py [-h] FILE

Basic file canary Python program

positional arguments:
  FILE        File to act as canary

optional arguments:
  -h, --help  show this help message and exit
```

### Example

```
python3 canary.py secrets.txt
```
