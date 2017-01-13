import sys
import java

lineSeparator = java.lang.System.getProperty("line.separator")
global AdminConfig

cellName = ""
nodeName = ""
serverName = ""
auth_alias = ""
driverPath = ""
datasource_name = ""
jndiName = ""
datasource_url = ""
jdbcProvider = ""
implementationClassName = ""
minConnections = ""
maxConnections = ""
datasource_helper_class = "give.specific.helper.class"

def createJDBCProvider(nodeName, serverName):
    print "Creating the database provider"
    n1 = ["name", jdbcProvider]
    implementationClassName = ["implementationClassName", implementationClassName]
    classPath = ["classPath", driverPath]
    description = ["description", jdbcProvider]

    jdbcAttrs = [n1, descriptionm implementationClassName, classPath]

    server = AdminConfig.getid("/Cell:" + cellName + "/Node:" + nodeName +
        "/Server:" + serverName + "/")
    AdminConfig.create("JDBCProvider", server, jdbcAttrs)
    print "jdbc provider creater"
    AdminConfig.save()


def createDS(nodeName, serverName):
    print("Creating Datasource: " + datasource_name + " Node: " + nodeName +
        " Server: " + serverName)
    jdbcProvider = AdminConfig.getid("/Cell:" + cellName + "/Node:" + nodeName +
        "/Server:" + serverName + "/JDBCProvider:" + jdbcProvider + "/")

    #create Data source
    auth_alias = ["authDataAlias", auth_alias]
    datasource_helper_class = ["datasourceHelperClassname", datasource_helper_class]
    description = ["description", datasource_name]
    jndi = ["jndiName", jndiName]
    name = ["name", datasource_name]
    datasource_attrs = [name, description, jndi, datasource_helper_class, auth_alias]
    
