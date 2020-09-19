import sys
from pathlib import Path
import gnupg

if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

def getDataFromEncryptedFile(encryptedFile):
    print("Safely opening encrypted file...")
    gpghome = str(Path.home()) + "/.gnupg/"
    gpg = gnupg.GPG(gnupghome = gpghome)
    with open(encryptedFile, 'rb') as f:
        return StringIO(str(gpg.decrypt_file(f)))
