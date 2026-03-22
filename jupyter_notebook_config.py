#
# Jupyter Notebook Configuration File
#
# Python for Algorithmic Trading
# (c) LI CHENYANG
# The Nirvana Project
#
# SSL ENCRYPTION
# replace the following file names (and files used) by your choice/files
c.NotebookApp.certfile = u'/root/.jupyter/mycert.pem'
c.NotebookApp.keyfile = u'/root/.jupyter/mykey.key'

# IP ADDRESS AND PORT
# set ip to '*' to bind on all IP addresses of the cloud instance
c.NotebookApp.ip = '0.0.0.0'
# it is a good idea to set a known, fixed default port for server access
c.NotebookApp.port = 8888

# PASSWORD PROTECTION
# here: 'jupyter' as password
# replace the hash code with the one for your password
c.NotebookApp.password = \
	'argon2:$argon2id$v=19$m=10240,t=10,p=8$09ik4t417koeSPRew1nEIg$QJ+a+RQB0vaWa/gtYKMo+oERp92kFeGvQHevIjdiIM8'

# NO BROWSER OPTION
# prevent Jupyter from trying to open a browser
c.NotebookApp.open_browser = False

# ROOT ACCESS
# allow Jupyter to run from root user
c.NotebookApp.allow_root = True
