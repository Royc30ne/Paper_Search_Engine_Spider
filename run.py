import IEEE_Xplore_spider as ixs

if __name__ == '__main__':
    # Enter the keywords that need to be searched here
    ieee = ixs.XploreSpider(r'("online risk*” OR "online abuse" OR "mental health") AND "deep learning"')
    ieee.operate()