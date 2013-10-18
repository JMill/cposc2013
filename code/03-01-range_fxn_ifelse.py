arthurDistance = 200
belindaDistance = 300
driverIs = "Arthur"

driveRange = belindaDistance - arthurDistance

if driverIs == "Arthur":
    print "Car travels only %s miles" % arthurDistance
else:
    print "Car goes %s to %s miles. Range: %s" % (arthurDistance, belindaDistance, driveRange)
