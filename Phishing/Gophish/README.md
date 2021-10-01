# Gophish Phishing Infrastructure Automation (AWS)

### Prequisites
1. An email account. I like using [Protonmail](https://protonmail.com/) since it's easy to create and destroy.
2. An SMTP server. I'll be using PostFix.
    - Install PostFix on Amazon AMI: `sudo yum install postfix`
      - Select the **Internet Site** option from the drop down and continue with the installation
      - Enter the email domain you want to use
    - Edit `/etc/postfix/main.cf` and make the following modifications:
      - Change the value of `myhostname` to `mail.[YOUR_DOMAIN].com`, example: `mail.phish.com`
      - Create a new variable called `mydomain` and set it to `[YOUR_DOMAIN].com`, example: `mydomain = phish.com`
3. Download and install [Terraform](https://www.terraform.io/downloads.html)

### Run

> Don't forget to change the AWS profile name in the `main.tf` file to your profile name

```bash
terraform init
terraform validate
terraform plan
terraform apply --auto-approve
```

### Obtaining the Admin Creds for Gophish Login
```bash
ssh -i id_rsa ec2-user@[EC2_INSTANCE_IP]
sudo cat /var/log/cloud-init-output.log | grep -oE '(Please.*)password\s[a-f0-9]+' | awk '{print $(NF-1),"=",$NF}'
```

> Login to Gophish interface at https://[EC2_INSTANCE_IP]:3333

> Enter the credentials admin:[PASSWORD]

### Creating Target Groups

### Creating Email Templates

### Creating Landing Pages

### Creating Sending Profiles

#### Sending Test Email

Before saving the profile, send a test email to your own test account to make sure you are successfully able to send emails.

### Creating Campaign
