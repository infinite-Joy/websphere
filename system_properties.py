"""
Set the system property for a JVM in websphere
"""

import sys
import java

global AdminConfig

# change the values here
cellName = ""
nodeName = ""
serverName = ""
endValue = ""


def createProperty(name, value):
    print "Creating System property: ", name, ": value = ", value
    nameAttr = ["name", name]
    valueAttr = ["value", value]
    attrs = [nameAttr, valueAttr]
    AdminConfig.create("Property", jvm, attrs, "systemProperties")


def main():
    server = AdminConfig.getid("/Cell:" + cellName + "/Node:" + nodeName +
                               "/Server:" + serverName + "/")
    jvm = AdminConfig.list("JavaVirtualMachine", server)
    createProperty("ENV", endValue)
    print "System property created"
    AdminConfig.save()


if __name__ == "__main__" or __name__ == "main":
    main()
