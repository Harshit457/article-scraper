from bs4 import BeautifulSoup
import requests
import sys
import validators

def scrape_pages(url):
    '''
    For scraping article and getting its title and body(p tags content)
    '''
    try:
        res = requests.get(url)

        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')

            title = soup.title.text

            p_content = soup.findAll('p')
            p_content = " ".join([p.text for p in p_content])

    except:
        print("Some exception occured.")

    return title, p_content

def write_to_file(filename,title, body):
    with open(f'{filename}.txt', 'w', encoding="utf-8") as f:
        f.write(title+'\n\n')
        f.write(body)
    print(title)
    print(body)

if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        
        moreInputs=True
        i=int(1)
        
        while(moreInputs):
            url=input("Enter the URL to scrap the article(Enter n/N to exit): ")
            if(url in ['n','N']): #Checking whether to stop the program or not
                break;
            
            if not validators.url(url):
                print(f"You have entered wrong URL({url}).")
                continue  # Go to the next iteration

            title, body = scrape_pages(url)
            write_to_file(i,title, body)
            i+=1
            
            
    else:
        for i,url in enumerate(sys.argv[1:]):

            if not validators.url(url):
                print(f"Invalid URL: {url}")
                continue  # Go to the next iteration

            title, body = scrape_pages(url)
            write_to_file(i,title, body)
