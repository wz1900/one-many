num = 0 ;
for line in open("temp.txt").readlines():
    line = line.strip() ;
    if( int(line) == 0  ): num = num + 1 ;

print num ;
