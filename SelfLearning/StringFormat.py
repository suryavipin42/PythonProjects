msg1 ="{0:s} is easier than {1:s}".format('python','java')
msg2 ="{1:s} is easier than {0:s}".format('python','java')

# 10.2f-> total length 10 and 2 decimals.
msg3 ="{:10.2f} and {:d}".format(1.234234234, 12)
msg4 = "{}".format(1.234234234)
print(msg1)
print(msg2)
print(msg3)
print(msg4)