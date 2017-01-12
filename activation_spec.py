import sys
import java
import  time
global AdminConfig

# Setting local time here
t = time.localtime()
asctime = time.asctime(t)
transType = ""
destType = ""
description = "this is for my application, created by jython script on" + asctime

#################################
cellName = ""
nodeName = ""
serverName = ""
queue_manager_host1 = ""
queue_manager_host2 = ""
queue_manager_nam1 = ""
queue_manager_nam2 = ""
resource_name1 = ""
resource_name2 = ""
queue_manager_port = ""
queue_serv_channel = "" # given as a string
destination_jndi_channel = ""

#####################################

def createActivationSpecifications(cell, node, server, provider, resource_name,
      res_jndi, queue_manager_name, queue_manager_host):
    serverId = AdminConfig.getid("/Cell:" + cell + "/Node:" + node +
        "/Server:" + server + "/")
    print("Creating activation specification resource for JVM " + serverId)

    # Creating the websphere MQ JMS Provider to create JMS activation spec
    jmsId = AdminConfig.getid("/Cell:" + cell + "/Node:" + node + "/Server:" +
       server + "/JMSProvider:" + provider + "/")
    print jmsId
    jmscreateId = AdminTask.createWMQActivationSpec(jmsId, "[-name ]" +
        resource_name + "-jndiName " + res_jndi + " -description " +
        destination + " -destinationJNDIName " + destinationJNDIName +
        " -destinationType " + destinationType + " -qMgrName" +
        queue_manager_name + " -wmqTransportType " + transportType +
        " -qmgrHostname " + queue_manager_host + " -qmgrPortNumber "
        + queue_manager_port + " -qmgrSvrconnChannel " +
        queue_serv_channel + " ]")

    AdminTask.createSSLConfigGroup("[-name " + serverName +
        " -direction outbound -certificateAlias default =scopeName (cell):" +
        cellName + ":(node):" + nodeName + ":(server):" + serverName +
        " -sslConfigAliasName " + SSL_ConfigName + " -sslConfigScopeName " +
        "(cell):" + cellName + ":(node):" + nodeName + ":(server):" +
        serverName + " ]")
