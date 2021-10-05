# Gophish Phishing Infrastructure Automation (AWS)

### Prequisites
1. AWS credential profile (`~/.aws/credentials`)
2. A Domain - We'll be using Amazon Route 53 to register a domain if you don't already have one.
3. An SMTP server - We'll be using AWS SES (Simple Email Server).
4. Download and install [Terraform](https://www.terraform.io/downloads.html)

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
