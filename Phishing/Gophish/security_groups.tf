resource "aws_security_group" "gophish_sg" {
  name = "Allow Gophish traffic"
  description = "Allow traffic to ports 22, 80, 3333, and 8025"

  ingress = [
    {
      description = "Allow SSH"
      from_port = 22 
      to_port = 22
      protocol = "tcp"
      cidr_blocks = [ "0.0.0.0/0" ]
      ipv6_cidr_blocks = []
      self = false
      prefix_list_ids = []
      security_groups = []
    },
    {
      description = "Allow HTTP"
      from_port = 80 
      to_port = 80
      protocol = "tcp"
      cidr_blocks = [ "0.0.0.0/0" ]
      ipv6_cidr_blocks = []
      self = false
      prefix_list_ids = []
      security_groups = []
    },
    {
      description = "Allow access to Gophish server"
      from_port = 3333
      to_port = 3333
      protocol = "tcp"
      cidr_blocks = [ "0.0.0.0/0" ]
      ipv6_cidr_blocks = []
      self = false
      prefix_list_ids = []
      security_groups = []
    },
    {
      description = "Allow MailHog access"
      from_port = 8025 
      to_port = 8025
      protocol = "tcp"
      cidr_blocks = [ "0.0.0.0/0" ]
      ipv6_cidr_blocks = []
      self = false
      prefix_list_ids = []
      security_groups = []
    }
  ]

  egress = [
    {
      description = "Allow outbound traffic to anywhere"
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = [ "0.0.0.0/0" ]
      ipv6_cidr_blocks = []
      self = false
      prefix_list_ids = []
      security_groups = []
    }
  ]
}
