import sys
import java

rolloverSize = "" # give in numbers
maxNumberOfBackupFiles = "" # gove in numbers

def updateLogPath(cellName, nodeName, serverName, baseLogPath):
    server = AdminConfig.getid("/Cell:" + cellName + "/Node:" + nodeName
        + "/Server:" + serverName + "/")

    # configure systemout.log and systemerror.log
    systemout_log = AdminConfig.showAttribute(server, "outputStreamRedirect")
    AdminConfig.modify(systemout_log,
        [["fileName", baseLogPath + "/SystemOut.log"],
        ["rolloverSize", rolloverSize],
        ["maxNumberOfBackupFiles", maxNumberOfBackupFiles]])
    systemerror_log = AdminConfig.showAttribute(server, "errorStreamRedirect")
    AdminConfig.modify(systemerror_log,
        [["fileName", baseLogPath + "/SystemError.log"],
        ["rolloverSize", rolloverSize],
        ["maxNumberOfBackupFiles", maxNumberOfBackupFiles]])
    print "SystemOut and SystemError log file locations updated"

    #configure native_stdout.log and native_stderror.log
    javaProc = AdminConfig.list("javaProcessDef", server)
    nativeLog = AdminConfig.showAttribute(javaProc, "ioRedirect")
    AdminConfig.modify(nativeLog,
        [["stdoutFilename", baseLogPath + "/native_stdout.log"]])
    AdminConfig.modify(nativeLog,
        [["stderrorFilename", baseLogPath + "/native_stderror.log"]])
    print "native_stdout.log and native_stderror.log log file locations updated"

    # Configure activity log
    rsaLoggingService = AdminConfig.list("RSALoggingService", server)
    activityLog = AdminConfig.showAttribute(rsaLoggingService, "serviceLog")
    AdminConfig.modify(activityLog, [["name", baseLogPath + "/activity.log"]])
    print "Activity log file locations updated"

    # Configure trace log
    traceService = AdminConfig.list("TraceService", server)
    traceLog = AdminConfig.showAttribute(traceService, "traceLog")
    AdminConfig.modify(traceLog, [["fileName", baseLogPath + "/trace.log"]])
    print "Trace Log File location updated"

    AdminConfig.save()
    print "AdminConfig save successfull for JVM - ", serverName


def main():
    updateLogPath("cell", "nodeName", "jvm1", "base/log/path")
    updateLogPath("cell", "nodeName", "jvm2", "base/log/path")


if __name__ == "__main__" or __name__ == "main":
    main()
