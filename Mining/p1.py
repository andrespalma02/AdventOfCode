from _sha256 import sha256


def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = '1' * difficulty
    for i in range(10000000):
        digest = sha256(str(hash(message + str(i))).encode('utf-16')).hexdigest()
        if digest.startswith(prefix):
            print("after " + str(i) + " iterations found nonce: " + digest)
            return digest


print(mine("test", 5))
