import sh
import sys
import re

def brute_force_a_records(base_domain, record_type):

    SUBDOMAINS = """
    www
    ftp
    mail
    owa
    proxy
    router
    admin
    www2
    firewall
    mx
    pop3
    mobile
    m
    """
    
    ips = []
    for subdomain in SUBDOMAINS.split():
        full_domain = subdomain.strip() + "." + base_domain
        print "Trying full_domain %s: " % full_domain

        try:
            host_out = sh.host("-t", record_type, full_domain)
            print host_out
            ips_new = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str(host_out) )
            ips += ips_new
            #was going to parse output, too unpredictable so fuck it
        except sh.ErrorReturnCode_1:
            continue

    return ips

def reverse_dns_discovery(ips):
    
    for ip in ips:
        ip = str(ip)
        ip = ip.split(".")
        for i in range(0, 255):
            ip[-1] = str(i)
            try:
                out = sh.host(".".join(ip))
                print out
            except sh.ErrorReturnCode_1:
                sys.stderr.write("Nothing found at %s\n" % ip)
        
if __name__ == "__main__":

    try:
        basename = sys.argv[1]
    except:
        print "Usage dns_brute.py dns_basename"
        sys.exit(1)
        
    ips = brute_force_a_records(basename, "A")
    print "Going to reverse lookup %s" % str(ips)
    reverse_dns_discovery(ips)
