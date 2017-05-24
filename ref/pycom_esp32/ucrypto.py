"""ucrypto — Cryptography
This module provides native support for cryptographic algorithms. It’s loosely based on PyCrypto ( http://pythonhosted.org/pycrypto/ ).

Warning: Cryptography is not a trivial business. Doing things the wrong way could quickly result in decreased or no security. Please document yourself in the subject if you are depending on encryption to secure important information.
"""

class AES(object):
    """class AES - Advanced Encryption Standard
AES (Advanced Encryption Standard) is a symmetric block cipher standardized by NIST. It has a fixed data block size of 16 bytes. Its keys can be 128, 192, or 256 bits long.

Note: AES is implemented using the ESP32 hardware module.

Usage:
    from crypto import AES
    import crypto
    key = b'notsuchsecretkey' # 128 bit (16 bytes) key
    iv = crypto.getrandbits(128) # hardware generated random IV (never reuse it)

    cipher = AES(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn')

    # ... after properly sent the encrypted message somewhere ...

    cipher = AES(key, AES.MODE_CFB, msg[:16]) # on the decryption side
    original = cipher.decrypt(msg[16:])
    print(original)

Warning: To avoid security issues, IV should always be a random number and should never be reused to encrypt two different messages. The same applies to the counter in CTR mode. You can use crypto.getrandbits() for this purpose.
    """
    def __init__(self, key, mode, IV, *, counter, segment_size):
        """Create an AES object that will let you encrypt and decrypt messages.
The arguments are:
    - key (byte string) is the secret key to use. It must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes long.
    - mode is the chaining mode to use for encryption and decryption. Default is AES.MODE_ECB.
    - IV (byte string) initialization vector. Should be 16 bytes long. It is ignored in modes AES.MODE_ECB and AES.MODE_CRT.
    - counter (byte string) used only for AES.MODE_CTR. Should be 16 bytes long. Should not be reused.
    - segment_size is the number of bits plaintext and ciphertext are segmented in. Is only used in AES.MODE_CFB. Supported values are AES.SEGMENT_8 and AES.SEGMENT_128.
        """
        super().__init__(key=key, mode=mode, IV=IV, counter=counter, segment_size=segment_size)
        pass
    def encrypt(data):
        """Encrypt data with the key and the parameters set at initialization."""
        return bytes()
    def decrypt(data):
        """Decrypt data with the key and the parameters set at initialization."""
        return bytes()
    
    MODE_ECB=int()
    MODE_CBC=int()
    MODE_CFB=int()
    MODE_CTR=int()

    SEGMENT_8=int()
    SEGMENT_128=int()

def getrandbits(bits):
    """Returns a bytes object filled with random bits obtained from the hardware random number generator.
According to the ESP32 Technical Reference Manual, such bits ”... can be used as the basis for cryptographical operations”. “These true random numbers are generated based on the noise in the Wi-Fi/BT RF system. When Wi-Fi and BT are disabled, the random number generator will give out pseudo-random numbers.”
The parameter bits is rounded upwards to the nearest multiple of 32 bits.
    """
    return bytes()
