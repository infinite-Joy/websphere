import sys
import java

global AdminConfig

# Common Variables
cellName = ""
nodeName = ""
serverName =- ""
listenerName1 = ""
listenerName2 = ""

queueName = "jms/samplequeue"

connFactory1 = "jms/connFactory1"
connFactory2 = "jms/connFactory2"


def createMessageListener(nodeName, serverName, name, destination, connFactory,
                          initState, mdbMaxSession, mdbMaxRet):
    serv = AdminConfig.getid("/Cell:" + cellName + "/Node:" + nodeName +
                             "/Server:" + serverName + "/")
    mls = AdminConfig.list("MessageListenerService", serv)
    print mls
    new_listener_port = AdminConfig.create("ListenerPort", mls, [["name", name],
        ["destinationJNDIName", destination],
        ["connectionFactoryJNDIName", connFactory],
        ["maxSessions", mdbMaxSession], ["maxRetries", mdbMaxRet],
        ["maxMessages", "1"]])
    print new_listener_port
    print AdminConfig.create("StateManageable", new,
                            [["initialState", initState]])
    print name + " Listener Port Created"
    AdminConfig.save()


def main():
    print "Creating message listener"
    createMessageListener(nodeName, serverName, listenerName1, queueName,
        connFactory, "START", "10", "2")
    print "done"


if __name__ == "__main__" or __name__ == "main":
    main()
