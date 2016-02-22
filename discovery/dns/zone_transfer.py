from dns_basic_discovery import get_nameservers
import sh
import sys

def zone_transfer(basename):
    out = get_nameservers(basename)
    for ns_line in out.split("\n"):
        if not ns_line:
            continue
        ns_line = ns_line.split()
        ns = ns_line[-1]
        print ns
        try:
            print "Trying %s"% ns
            sh.host("-l", ns)
        except sh.ErrorReturnCode_1:
            sys.stderr.write("Zone transfer failed on %s\n" % ns)

if __name__ == "__main__":
    zone_transfer("google.com")
