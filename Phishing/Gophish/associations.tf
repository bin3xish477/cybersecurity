resource "aws_route_table_association" "rt_associations" {
  subnet_id = "${aws_subnet.public_subnet.id}"
  route_table_id = "${aws_route_table.public_rtb.id}"
}
