import magneturi
import base64

"""
获取种子的hash值
"""
def hash_bt(file_path):
    magnet_link = magneturi.from_torrent_file(file_path)
    hash32=magnet_link[20:52]
    b16_hash = base64.b16encode(base64.b32decode(hash32))
    b16_hash = b16_hash.lower()
    return str(b16_hash,"utf-8")

def get_magnet(bt_hash):
    return 'magnet:?xt=urn:btih:'+bt_hash