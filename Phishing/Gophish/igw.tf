resource "aws_internet_gateway" "igw" {
  vpc_id = "${aws_vpc.gophish_vpc.id}"
  tags = {
    Name = "gophish-igw"
  }
}
