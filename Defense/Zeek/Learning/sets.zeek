event zeek_init()
    {
    local s: set[string] = {"one", "two", "three"};
    # adding element to set
    add s["four"];

    # deleting element from set
    delete s["two"];

    # checking membership of element in set
    print "one" in s;

    # printing all elements in set
    for (w in s)
        {
            print w;
        }
    }
