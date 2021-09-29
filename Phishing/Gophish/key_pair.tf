resource "aws_key_pair" "gophish_ssh_key" {
  key_name = "gophish-ssh-key"
  public_key = "${file("id_rsa.pub")}"
}
