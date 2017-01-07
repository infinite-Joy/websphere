import java.lang.System as sys
lineSeparator = sys.getProperty("line.separator")

global AdminConfig

# Common Variables
cellName = ""
nodeName = ""
serverName = ""
connectionFactory1 = ""
connectionFactory2 = ""
queueServer1 = "" # MQ server host name
queueServer2 = "" # MQ server host name in cluster
queueManager1 = "" # queue manager name
queueManager2 = "" # queue manager name in cluster
mqPort = ""
queueName1 = ""
baseQueueName1 = ""
queueName2 = ""
baseQueueName2 = ""


def createMQCF(nodeName, serverName, name, jndi, queue_manager,
        host, port, channel):
    print "Create Websphere MQ Connection Factory Resource ..." + name
    jmsProvider = AdminConfig.getid("/Cell:" + cellName + "/Node:" + nodeName
        + "/Server:" + serverName + "/JMSProvider:Websphere MQ JMS Provider")
    templateQCF_string = AdminConfig.listTemplates("MQConnectionFactory")
    templateQCF = templateQCF_string.split(lineSeparator)[0]
    conn_factory_name = ["name", name]
    conn_factory_jndi_name = ["jndi", name]
    conn_factory_description = ["description", name]
    mapConfig = ["mapping", [["mappingConfigAlias", "DefaultPrincipalMapping"],
        ["authDataAlias", ""]]]
    queue_manager_name = ["queueManager", queue_manager]
    host_name = ["host", host]
    port_number = ["port", port]
    channel_name = ["channel", channel]
    transport_type = ["transportType", "CLIENT"]
    message_retention_flag = ["msgRetention", "true"]
    xa_flag = ["XAEnabled", "true"]
    pool_attrs = [["agedTimeout", 0],
        ["connectionTimeout", 180], ["maxConnections", 10],
        ["minConnections", 1], ["purgePolicy", "EntirePool"],
        ["reapTime", "180"], ["unusedTimeout", "1800"]]
    connectionPool = ["connectionPool", pool_attrs]
    sessionPool = ["sessionPool", pool_attrs]
    connection_factory_attr = [conn_factory_name, conn_factory_jndi_name,
        conn_factory_description, mapConfig, queue_manager_name, host_name,
        port_number, channel_name, transport_type, message_retention_flag,
        xa_flag, connectionPool, sessionPool]
    AdminConfig.createUsingTemplate("MQConnectionFactory", jmsProvider,
        connection_factory_attr, templateQCF)
    print "Websphere MQ Connection Factory Resource created: " + name

    AdminConfig.save()
