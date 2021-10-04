resource "aws_route_table" "public_rtb" {
  vpc_id = "${aws_vpc.gophish_vpc.id}"
  route {
      cidr_block = "0.0.0.0/0"
      gateway_id = "${aws_internet_gateway.igw.id}"
    }
}
