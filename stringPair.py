#string pair
# a e i o u


def solve2(arr,d):
    count=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]==d):
                count+=1
                #print(arr[i],arr[j])
    return count
    

def solve(arr):
    
    number={0:['zero',2],
        1:['one',2],
       2:['two',1],
       3:['three',2],
       4:['four',2],
       5:['five',2],
       6:['six',1],
       7:['seven',2],
       8:['eight',2],
       9:['nine',2],
       10:['ten',1],
       11:['eleven',3],
       12:['twelve',2],
       13:['thirteen',3],
       14:['fourteen',4],
       15:['fifteen',3],
       16:['sixteen',3],
       17:['seventeen',4],
       18:['eighteen',3],
       19:['nineteen',4],
       20:['twenty',1],
       21:['twentyone',3],
       22:['twentytwo',2],
       23:['twentythree',3],
       24:['twentyfour',3],
       25:['twentyfive',3],
       26:['twentysix',2],
       27:['twentyseven',3],
       28:['twentyeight',3],
       29:['twentynine',3],
       30:['thirty',1],
       31:['thirtyone',3],
       32:['thirtytwo',2],
       33:['thirtthree',3],
       34:['thirtyfour',3],
       35:['thirtyfive',3],
       36:['thirtysix',2],
       37:['thirtyseven',3],
       38:['thirtyeight',3],
       39:['thirytnine',3],
       40:['forty',1],
       41:['fortyone',3],
       42:['fortytwo',2],
       43:['fortythree',3],
       44:['fortyfour',3],
       45:['fortyfive',3],
       46:['fortysix',2],
       47:['fortyseven',3],
       48:['fortyeight',3],
       49:['fortynine',3],
       50:['fifty',1],
       51:['fiftyone',3],
       52:['fiftytwo',2],
       53:['fiftythree',3],
       54:['fiftyfour',3],
       55:['fiftyfive',3],
       56:['fiftysix',2],
       57:['fiftyseven',3],
       58:['fiftyeight',3],
       59:['fiftynine',3],
       60:['sixty',1],
       61:['sixtyone',3],
       62:['sixtytwo',2],
       63:['sixtythree',3],
       64:['sixtyfour',3],
       65:['sixtyfive',3],
       66:['sixtysix',2],
       67:['sixtyseven',3],
       68:['sixtyeight',3],
       69:['sixtynine',3],
       70:['seventy',2],
       71:['seventyone',4],
       72:['seventytwo',3],
       73:['seventythree',4],
       74:['seventyfour',4],
       75:['seventyfive',4],
       76:['seventysix',3],
       77:['seventyseven',4],
       78:['seventyeight',4],
       79:['seventynine',4],
       80:['eighty',2],
       81:['eightyone',4],
       82:['eightytwo',3],
       83:['eightythree',4],
       84:['eightyfour',4],
       85:['eightyfive',4],
       86:['eightysix',3],
       87:['eightyseven',4],
       88:['eightyeight',4],
       89:['eightynine',4],
       90:['ninety',2],
       91:['ninetyone',4],
       92:['ninetytwo',3],
       93:['ninetythree',4],
       94:['ninetyfour',4],
       95:['ninetyfive',4],
       96:['ninetysix',3],
       97:['ninetyseven',4],
       98:['ninetyeight',4],
       99:['ninetynine',4],
       100:['hundred',2]
        }

    d=0
    for i in arr:
        d+=number[i][1]
   
    ans=solve2(arr,d)
    #print(d)
    if(ans>100):
        k='greater 100'
    else:
        k=number[ans][0]
    return k
        
    

if __name__=="__main__":
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(solve(arr))
