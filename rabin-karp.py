
 
def search_for_pat(pat, txt,d, q):
    M = len(pat)
    N = len(txt)
    p_hash = 0    # records hash value corresponding to query pattern
    t_hash = 0    # records hash value corresponding to text
    h = 1

    for i in xrange(M-1):
        h = (h*d)%q
 
    # Calculate the hash value of pattern and text having length equal to pattern
    for i in xrange(M):
        p_hash = (d*p_hash + ord(pat[i]))%q
        t_hash = (d*t_hash + ord(txt[i]))%q
 
    # check for the matching pattern
    for i in xrange(N-M+1):
        # Check the hash values of p_hash and t_hash. The patterns are compared if the hash value matches
        
        if p_hash==t_hash:
            # Check for characters one by one
            for j in xrange(M):
                if txt[i+j] != pat[j]:
                    break
 
            j+=1

            if j==M:
                print "Pattern found at index " + str(i)
 
        if i < N-M:
            t_hash = (d*(t_hash - ord(txt[i])*h) + ord(txt[i+M]))%q

            if t_hash < 0:
                t_hash = t_hash+q

def main():
    txt = "THE FOLLOWING ALGORITHM HELPS IN SUBSTRING FINDING"
    pat = "HELP"
    q = 101 # A prime number
    d=256
    search_for_pat(pat,txt,d,q)



if __name__=="__main__":
    main()
