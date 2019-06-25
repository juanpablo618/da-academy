import sys

current_item = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    item, count = line.split("\t")    

    try:
        count = int(count)
    except ValueError:
            continue    

    if current_item == item:
            current_count += count #1        

    else:
            if current_item:
                print '%s\t%s' % (current_item, current_count)

            current_item = item
            current_count = count            

if current_item == item:   #ultima iteración
        print '%s\t%s' % (current_item, current_count)

                