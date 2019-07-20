# Set options for certfile, ip, password, and toggle off

# browser auto-opening

# c.NotebookApp.certfile = u'/absolute/path/to/your/certificate/mycert.pem'

# c.NotebookApp.keyfile = u'/absolute/path/to/your/certificate/mykey.key'

# Set ip to '*' to bind on all interfaces (ips) for the public server

c.NotebookApp.ip = '*'

# Put your sha password here
# password is "jupyter"
c.NotebookApp.password = u'sha1:13f20fce2676:5f388033b2df5ada9140adb045c06b2d6bb238d2'
c.NotebookApp.open_browser = False

# It is a good idea to set a known, fixed port for server access

c.NotebookApp.port = 6969
