from jsonrpc import ServiceProxy
access = ServiceProxy("http://111.90.140.12:46261")
pwd = raw_input("Enter wallet passphrase: ")
access.walletpassphrase(pwd, 60)
