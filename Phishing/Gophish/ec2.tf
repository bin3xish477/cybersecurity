resource "aws_instance" "gophish_instance" {
  ami = "ami-087c17d1fe0178315"
  instance_type = "t2.micro"
  key_name = "${aws_key_pair.gophish_ssh_key.key_name}"

  tags = {
    Name = "gophish-instance"
  }

  vpc_security_group_ids = [ aws_security_group.gophish_sg.id ]

  # Base64 encoded string of the `user-data.sh` Bash script in the current directory
  user_data_base64 = "IyEvYmluL2Jhc2gKCm1rZGlyIC9vcHQvZ29waGlzaApjZCAvb3B0L2dvcGhpc2gKd2dldCAtTyBnb3BoaXNoLnppcCBodHRwczovL2dpdGh1Yi5jb20vZ29waGlzaC9nb3BoaXNoL3JlbGVhc2VzL2Rvd25sb2FkL3YwLjExLjAvZ29waGlzaC12MC4xMS4wLWxpbnV4LTY0Yml0LnppcAp1bnppcCBnb3BoaXNoLnppcApzZWQgLWkgJ3N8MTI3XC4wXC4wXC4xfDBcLjBcLjBcLjB8ZycgY29uZmlnLmpzb24KY2htb2QgK3ggLi9nb3BoaXNoCi4vZ29waGlzaAoK"
}
