global local_subnets: set[subnet] = {
									    192.168.1.0/24,
									    192.68.2.0/24,
									    172.16.0.0/20,
									    172.16.16.0/20,
									    172.16.32.0/20,
									    172.16.48.0/20
									};
global inside_local_network: set[addr];
global outside_local_network: set[addr];

event new_connection(c: connection)
	{
	if (c$id$orig_h in local_subnets)
		{
		add inside_local_network[c$id$orig_h];
		}
	else
		add outside_local_network[c$id$orig_h];
	
	if (c$id$resp_h in local_subnets)
		{
		add inside_local_network[c$id$resp_h];
		}
	else
		add outside_local_network[c$id$resp_h];
	}
	
event zeek_done()
	{
	print("IP's inside local network");
	for (local_ip in inside_local_network)
		{
		print(local_ip);
		}
	print("IP's outside local network");
	for (external_ip in outside_local_network)
		{
		print(external_ip);
		}
	}
