global myevent: event(s: string);

global n = 0;

event myevent(s: string) &priority = -10
	{
	++n;
	}

event myevent(s: string) &priority = 10
	{
	print "myevent", s, n;
	}

event zeek_init()
	{
	print "zeek_init()";
	event myevent("hi");
	schedule 5 sec { myevent("bye") };
	}

event zeek_done()
	{
	print "zeek_done()";
	}
