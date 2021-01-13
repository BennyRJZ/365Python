# Complete the function/method so that it returns the url with anything 
# after the anchor (#) removed.

# # returns 'www.codewars.com'
# remove_url_anchor('www.codewars.com#about')

# # returns 'www.codewars.com?page=1' 
# remove_url_anchor('www.codewars.com?page=1') 

#url https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python
def remove_url_anchor(url):
    limit = 0
    
    for i in range(0,len(url)):
        if url[i] == '#':
            print(url[i])
            limit = i
            print(limit)
            break
        else:
            print(i)
    if limit == 0:
        limit=len(url)
    return(url[:limit])