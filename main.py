import requests
from bs4 import BeautifulSoup

def fetch_news(url): #function to fetch and parse the HTML content of the website
    base_url = "https://bbc.com" #base url for most anchor tags
    response = requests.get(url)
    
    if response.status_code == 200: #if response ok parse using bs4
        soup = BeautifulSoup(response.content, 'html.parser')
        
        stories = soup.find_all('div', attrs={'data-testid': 'anchor-inner-wrapper'}) #find all divs which contain a link to a news story
        
        news_list = []
        seen_titles = set()  #set to avoid displaying duplicates of news

        for story in stories:
            link_tag = story.find('a', attrs={'data-testid': 'internal-link'}) or story.find('a', attrs={'data-testid': 'external-anchor'}) #get link to story using either of the two link attributes
            if link_tag and 'href' in link_tag.attrs: #set the link to the stroy according to its base url
                link = base_url + link_tag['href'] if link_tag['href'].startswith('/') else link_tag['href']
            else:
                continue  #skip the anchor tag if it has no valid link
            
            title_tag = story.find('h2', attrs={'data-testid': 'card-headline'}) #find the title of the story
            if title_tag: #extract and format the title
                title = title_tag.get_text().strip()
            else:
                continue  #skip the h2 tag if there is no valid link
            
            summary_tag = story.find('p', attrs={'data-testid': 'card-description'}) #find the summary of the story
            if summary_tag:
                summary = summary_tag.get_text().strip() #extract and format the sumamry
            else:
                continue  #skip the p tag if there is no summary

            if title not in seen_titles:  #check if the title is already in the set, if not then add it otherwise ignore
                seen_titles.add(title)
                news_list.append({'title': title, 'link': link, 'summary': summary})
        
        return news_list
    else:
        print("Failed to retrieve the page.")
        return []


def display_news(news_list, keyword=None): #display function

    if keyword: #if a keyword is given, filter the news accordingly
        keyword_lower = keyword.lower()
        filtered_news = [
            news for news in news_list
            if keyword_lower in news['title'].lower() or keyword_lower in news['summary'].lower()
        ]
    else: #else just give the whole news list
        filtered_news = news_list 

    if filtered_news: #sisplay the filtered news
        for idx, news in enumerate(filtered_news, start=1): #for loop to go through the lsit and number and display the news
            print(f"{idx}. {news['title']}")
            print(f"   Summary: {news['summary']}")
            print(f"   Link: {news['link']}\n")
    else:
        print("No news available matching the keyword.")

if __name__ == "__main__":
    url = "https://bbc.com/news"

    news_list = fetch_news(url)

    keyword = input("Enter a keyword to filter the news (or press Enter to show all news): ")

    display_news(news_list, keyword)
    