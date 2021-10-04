resource "aws_instance" "gophish_instance" {
  subnet_id = "${aws_subnet.public_subnet.id}"
  ami = "${var.ami}"
  instance_type = "${var.instance_type}"
  key_name = "${aws_key_pair.gophish_ssh_key.key_name}"

  tags = {
    Name = "gophish-instance"
  }

  vpc_security_group_ids = [ aws_security_group.gophish_sg.id ]

  # Base64 encoded string of the `user-data.sh` Bash script in the current directory
  user_data_base64 = "IyEvYmluL2Jhc2gKCmdvcGhpc2hfc2V0dXAoKSB7CiAgbWtkaXIgL29wdC9nb3BoaXNoCiAgY2QgL29wdC9nb3BoaXNoCiAgd2dldCAtTyBnb3BoaXNoLnppcCAnaHR0cHM6Ly9naXRodWIuY29tL2dvcGhpc2gvZ29waGlzaC9yZWxlYXNlcy9kb3dubG9hZC92MC4xMS4wL2dvcGhpc2gtdjAuMTEuMC1saW51eC02NGJpdC56aXAnCiAgdW56aXAgZ29waGlzaC56aXAKICBybSBnb3BoaXNoLnppcAogIHNlZCAtaSAnc3wxMjdcLjBcLjBcLjF8MFwuMFwuMFwuMHxnJyBjb25maWcuanNvbgogIGNobW9kICt4IC4vZ29waGlzaAogIC4vZ29waGlzaCAmCn0KCm1haWxob2dfc2V0dXAoKSB7CiAgIyBVc2UgbWFpbGhvZyBhcyB0aGUgc2VuZGluZyBTTVRQIHNlcnZlcgogIG1rZGlyIC9vcHQvbWFpbGhvZwogIGNkIC9vcHQvbWFpbGhvZwogIHdnZXQgLU8gbWFpbGhvZyAnaHR0cHM6Ly9naXRodWIuY29tL21haWxob2cvTWFpbEhvZy9yZWxlYXNlcy9kb3dubG9hZC92MS4wLjEvTWFpbEhvZ19saW51eF9hbWQ2NCcKICBjaG1vZCAreCAuL21haWxob2cKICAuL21haWxob2cgJgp9Cgpnb3BoaXNoX3NldHVwCm1haWxob2dfc2V0dXAK"
}
