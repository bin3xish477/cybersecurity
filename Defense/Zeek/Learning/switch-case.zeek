event zeek_init() 
	{ 
	local str: string = "write a switch to count vowels!";
	local cnt: count = 0;
	
	for (c in str)
		{
	    switch (c)
			{
			case "a", "e", "i", "o", "u":
				cnt += 1;
				break;
			}
		}
	print fmt("Number of vowels: %s", cnt);
	}
