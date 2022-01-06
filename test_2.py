import hashlib

def is_eq_str(a, b):
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()
    return ha == hb

aboba = is_eq_str("next", "next")
print(aboba)

obabo = is_eq_str("next", "nest")
print(obabo)
