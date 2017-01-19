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

    AdminTask.createKeyStore("[ -scopeName (cell):" + cellName
        + ":(node):" + nodeName + ":(server):" + serverName
        + " -keyStoreName " + keyStoreName
        + " - keyStoreType JKS - keyStoreLocation "
        + JKSKeyStorePath + " -keyStorePassword " + keyPassword
        + " -keyStorePasswordVerify " + keyPassword
        + "keyStoreisFileBased true -keyStoreReadOnly false")
