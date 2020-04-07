import hashlib


class HashUtils(object):
    
    
    @staticmethod
    def md5(string: str):
        md5 = hashlib.md5(string.encode("utf-8"))
        return md5.hexdigest()
    
    @staticmethod
    def sha1(string: str):
        sha1 = hashlib.sha1(string.encode("utf-8"))
        return sha1.hexdigest()
    
    @staticmethod
    def sha256(string: str):
        sha256 = hashlib.sha256(string.encode("utf-8"))
        return sha256.hexdigest()
   
   
if __name__ == '__main__':
    print(HashUtils.sha1("wen"))