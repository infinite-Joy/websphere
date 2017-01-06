import sys
import java
global AdminConfig

cellName = "cellname"
alias = "<alias string>"
dbuser = "<give the db user>"
dbpwd = "give the db password"

def create_JAAS_auth_alias(auth_alias_name, user, password):
	print " - Creating JAAS auth alias: ", auth_alias_name

	# creating authaurisation data at the cell level
	security = AdminConfig.getid("/Cell:" + cellName + "/Security:/")
	jaasAttrs = [["alias", auth_alias_name], ["userId", user], ["password", password],
	            ["description", "Created by Jython Script for the user name" + user]]

	authDataAlias = AdminConfig.create("JAASAuthData", security, jaasAttrs)

	print " - Created JAAS Authentication Alias : - " + authDataAlias


if __name__ == "__main__" or __name__ == "main":
	create_JAAS_auth_alias(alias, dbuser, dbpwd)
	AdminConfig.save()