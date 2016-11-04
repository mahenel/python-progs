while 1 :
    print """
    1.windows
    2.linux
    3.mac
    4.quit
    """
    os = raw_input("select a option :")


    if os == '1' :
        print "windows os is selected"

    elif os == '2' :
        print "linux os is selected"

    elif os == '3' :
        print "mac os is selected"

    elif os == '4' :
        print 'good bye'

    else :
        print"invalid option selected"
        break