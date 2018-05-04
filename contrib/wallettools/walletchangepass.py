from jsonrpc import ServiceProxy
access = ServiceProxy("http://111.90.140.12:46261")
pwd = raw_input("Enter old wallet passphrase: ")
pwd2 = raw_input("Enter new wallet passphrase: ")
access.walletpassphrasechange(pwd, pwd2)
