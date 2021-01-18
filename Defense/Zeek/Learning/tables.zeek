event zeek_init()
    {
    local t: table[count] of string = {
        [1] = "value1",
        [2] = "value2",
        [3] = "value3"};

    # adding elements to table
    t[4] = "value4";

    # testing membership
    print "value4" in t;

    # deleting element from table
    delete t[1];

    # altering value for a table key
    t[2] = "val2";

    # print keys of a table
    for (k in t)
        {
        print k
        }
    }
