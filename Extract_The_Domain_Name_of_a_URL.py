'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
'''
def domain_name(url):
    if "http://"in url:
        url_list = url.split("/")
        url_list1 = url_list[2].split(".")
        if url_list1[0] == "www":
            return(url_list1[1])
        else:
            return(url_list1[0])
    elif "https://" in url:
        url_list = url.split("/")
        url_list1 = url_list[2].split(".")
        if url_list1[0] == "www":
            return(url_list1[1])
        else:
            return(url_list1[0])
    else:
        url_list = url.split(".")
        if url_list[0] == "www":
            return(url_list[1])
        else:
            return(url_list[0])