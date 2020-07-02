class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(val):
            vals = val.split('.')
            if len(vals) == 4:
                for v in vals:
                    try:
                        if ((len(v) > 1) and (v[0] == '0')) or (v[0] == '-') or (int(v) > 255):
                            return False
                    except:
                        return False
                return True
            return False
        def isIPv6(val):
            lens = set((1, 2, 3, 4))
            hexs = set(tuple(range(int('0', 16), int('FFFF', 16))))
            vals = val.split(':')
            if len(vals) == 8:
                for v in vals:
                    try:
                        if (int(v, 16) not in hexs):
                            return False
                    except:
                        return False
                    if (len(v) not in lens) or (v[0]=='-'):
                        return False
                return True
            return False
        if isIPv4(IP):
            return 'IPv4'
        if isIPv6(IP):
            return 'IPv6'
        return 'Neither'