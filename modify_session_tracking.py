import java.lang.System as sys

cellName = ""
nodeName = ""
serverName = ""
cookieName = ""


def modifySessionTracking(serverName, nodeName, cellName, cookieName):
    print "Updating Session Tracking Settings for ..." + "Server: " + serverName
        + " Cell: " + cellName + "Node:" + nodeName
    server = AdminConfig.getid("/Cell:" + cellName + "/Node:" + nodeName +
                             "/Server:" + serverName + "/")
    session_manager = AdminConfig.list("SessionManager", server)
    AdminConfig.modify(session_manager, [["enableCookies", "true"],
        "defaultCookieSettings", [["name", cookieName], ["secure", "true"]]])
    print "Saving Changes..."
    AdminConfig.save()


def main():
    modifySessionTracking(serverName, nodeName, cellName, cookieName)


if __name__ == "__main__" or __name__ == "main":
    main()
