# Please modify this file as needed, see the local.py.example for details:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example
#
# Importing docker provides common settings, see:
# https://github.com/benhutchins/docker-taiga/blob/master/docker-settings.py
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py
from .docker import *

PUBLIC_REGISTER_ENABLED = False
DEBUG = True
TEMPLATE_DEBUG = True

## Slack
# https://github.com/taigaio/taiga-contrib-slack
#INSTALLED_APPS += ["taiga_contrib_slack"]

## LDAP
# see https://github.com/ensky/taiga-contrib-ldap-auth
INSTALLED_APPS += ["taiga_contrib_ldap_auth"]

LDAP_SERVER = 'ldap://your_ip_server'
LDAP_PORT = 389

# Full DN of the service account use to connect to LDAP server and search for login user's account entry
# If LDAP_BIND_DN is not specified, or is blank, then an anonymous bind is attempated
LDAP_BIND_DN = 'CN=username,OU=group1,OU=group2,OU=group3,DC=domain,DC=damain,DC=domain'
LDAP_BIND_PASSWORD = 'CN_password'   # eg.
# Starting point within LDAP structure to search for login user
LDAP_SEARCH_BASE = 'DC=domain,DC=domain,DC=domain'
# LDAP property used for searching, ie. login username needs to match value in sAMAccountName property in LDAP
LDAP_SEARCH_PROPERTY = 'sAMAccountName'
LDAP_SEARCH_SUFFIX = None # '@example.com'

# Names of LDAP properties on user account to get email and full name
LDAP_EMAIL_PROPERTY = 'mail'
LDAP_FULL_NAME_PROPERTY = 'displayName'

## For additional configuration options, look at:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example
