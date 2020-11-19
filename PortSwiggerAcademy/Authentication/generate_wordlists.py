def main():
   with open("mod_usernames.txt", 'w') as f:
        f.truncate(0)
        f.seek(0)
        for i in range(200):
            if i % 2 == 0: f.write("carlos\n")
            else: f.write("wiener\n")

   with open("passwords.txt", 'r') as r:
        with open("mod_passwords.txt", 'w') as w:
            passwords = r.readlines()
            w.seek(0)
            for i in range(100):
                w.write(passwords[i])
                w.write("peter\n")
main()
