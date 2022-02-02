import IEEE_Xplore_spider as ixs

if __name__ == '__main__':
    # Enter the keywords that need to be searched here
    search_title = r'("online risk*” OR "online abuse" OR "mental health") AND "deep learning"'
    ieee = ixs.XploreSpider(search_title)
    ieee.operate()