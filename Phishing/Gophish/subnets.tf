resource "aws_subnet" "public_subnet" {
  vpc_id = "${aws_vpc.gophish_vpc.id}"
  cidr_block = "${var.public_subnet_cidr}"
  map_public_ip_on_launch = true
  availability_zone = "${var.az}"
  tags = {
    Name = "public-subnet-67354a08"
  }
}
