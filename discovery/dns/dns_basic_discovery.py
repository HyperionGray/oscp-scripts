import sh
import sys

def get_nameservers(basename):

    out = None
    try:
        out = sh.host("-t", "ns", basename)
#        print str(out)
    except sh.ErrorReturnCode_1:
        sys.stderr.write("No name servers found")

    return out
        
def get_mail_servers(basename):

    out = None
    try:
        out = sh.host("-t", "mx", basename)
#        print str(out)
    except sh.ErrorReturnCode_1:
        sys.stderr.write("No mail servers found")    

    return out
        
def get_cname_records(basename):

    out = None
    try:
        out = sh.host("-t", "cname", basename)
#        print str(out)
    except sh.ErrorReturnCode_1:
        sys.stderr.write("No cname records found")    

    return out
        
def get_soa_record(basename):
    
    out = None
    try:
        out = sh.host("-t", "soa", basename)
#        print str(out)
    except sh.ErrorReturnCode_1:
        sys.stderr.write("No soa records found")    

    return out
        
def get_txt_records(basename):

    out = None
    
    try:
        out = sh.host("-t", "txt", basename)
#        print str(out)
    except sh.ErrorReturnCode_1:
        sys.stderr.write("No txt records found")

    return out
        
if __name__ == "__main__":

    try:
        basename = sys.argv[1]
    except:
        print "Usage: dns_basic_discovery dns_basename"
        sys.exit(1)

    print "NS:"
    print get_nameservers(basename)
    print "MX:"
    print get_mail_servers(basename)
    print "CNAME:"
    print get_cname_records(basename)
    print "TXT:"
    print get_txt_records(basename)
