from bs4 import BeautifulSoup
import requests
import json
import re


# citations_needed = soup.find_all("")


def get_citations_needed_count(URL):
    '''
    calculate citations needed 

    args:
        url

    return:
        integer
    '''
    page = requests.get(URL) # <Response [200]>

    # conver from byte tp html
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    # resources = soup.find_all('sup',class_='reference')

    resources = soup.find_all('a', title='Wikipedia:Citation needed')

    return resources.__len__()
    # while resources == [citation needed]
    # for Citation in resources:
    #     citations_needed = Citation.find('a',title_='Wikipedia:Citation needed')
    #     print(citations_needed)

    # citations_needed = [citations_needed for Citation in resources]
    # print(Citation)
    # citations_needed = resources.find('a',title_='Wikipedia:Citation needed').text.strip()
    # print(citations_needed)


def get_citations_needed_report(URL):
    '''
    get citations needed report

    args:
        url
    return:
        report string
    '''
    page = requests.get(URL) # <Response [200]>

    soup = BeautifulSoup(page.content, 'html.parser')
    paragraph = soup.find_all('p')
    report = []

    for p in paragraph:

        if p.find('a', title= 'Wikipedia:Citation needed'):
            report.append(p.text.strip())
            res = '\n\n'.join(report)
    return res


if __name__ == '__main__':
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
