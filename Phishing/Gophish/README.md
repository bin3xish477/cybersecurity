# Gophish Phishing Infrastructure Automation (AWS)

### Prequisites
1. An email account. I like using [Protonmail](https://protonmail.com/) since it's easy to create and destroy.
2. An SMTP server. I'll be using [ElasticMail](https://elasticemail.com/) since it's free and easy to setup. You can obviously use the SMTP provided by what email service you use (Gmail, Office, etc).
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

> Login to Gophish interface at https://[EC2@_INSTANCE_IP]:3333

> Enter the credentials admin:[PASSWORD]

### Creating Target Groups

### Creating Email Templates

### Creating Landing Pages

### Creating Sending Profiles

#### Sending Test Email

### Creating Campaign
