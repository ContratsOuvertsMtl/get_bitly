#!/usr/local/bin/python
# coding: utf8


import bitly_api


def get_lien_court(url):

    """Obtenir le lien court"""
    c = bitly_api.Connection(access_token="e23e20fb2ff5afb3fd35c906f85c35029d699eb2")
    
    sh = c.shorten(url)
    
    return sh['url']

    
def main():
 
    lien_court = get_lien_court('http://google.com/')
    
    print(lien_court)
    
    return None
    
    
if __name__ == '__main__':
   main()
