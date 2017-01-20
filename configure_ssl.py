"""
This script will configure the JVM SSL outbound certificate Configuration
"""

import sys
import java
global AdminConfig

# set the JKS key store path
JKSKeyStorePath = "/path/to/JKS"
keyPassword = ""

def configureSSLConfiguration(cellName, nodeName, serverName, applicationName):
    keystoreName = applicationName + "_TS_CONFIG"
    print "Creating key store at the server level scope: " + keystoreName

    cell_node_server_scope = "(cell):" + cellName\
        + ":(node):" + nodeName + ":(server):" + serverName

    AdminTask.createKeyStore("[ -scopeName " + cell_node_server_scope
        + " -keyStoreName " + keyStoreName
        + " - keyStoreType JKS - keyStoreLocation "
        + JKSKeyStorePath + " -keyStorePassword " + keyPassword
        + " -keyStorePasswordVerify " + keyPassword
        + "keyStoreisFileBased true -keyStoreReadOnly false")

    SSL_ConfigName = serverName + "_SSL_CONFIG"
    AdminTask.createSSLConfigGroup("[ -alias " + SSL_ConfigName
        + " -scopeName " + cell_node_server_scope + " -trustStoreName " + keyStoreName
        + " -trustStoreScopeName " + cell_node_server_scope
        + " -keyStoreName CellDefaultKeyStore -keyStoreScopeName (cell):"
        + cellName + " ]")

    print " Created SSL config .. " + SSL_ConfigName

    AdminTask.createSSLConfigGroup("[-name " + serverName
       + " -direction outbound -certificateAlias default -scopeName"
       + cell_node_server_scope + " -sslConfigAliasName " + SSL_ConfigName
       + " -sslConfigScopeName " + cell_node_server_scope + "]")

    AdminConfig.save()

    print " SSL configuration has been successfully configured for the server: " + serverName


def main():
    configureSSLConfiguration("cell", "node", "server", "app")


if __name__ == "__main__" or __name__ == "main":
    main()
