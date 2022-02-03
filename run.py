import IEEE_Xplore_spider as ixs

if __name__ == '__main__':
    # Enter the keywords that need to be searched here
    while(True):
        print("========================================")
        print("=           Paper Crawler              =")
        print("=          Author: Royc30ne            =")
        print("=  A Higher Place: WWW.ROYC30NE.COM    =")
        print("=              Enjoy It!               =")
        print("=             Ver. 0.1.0               =")
        print("========================================")
        print("Enter number to choose paper search engine:")
        print("1. IEEE Xplore")
        print("2. ACM Digit Library (Under Construction)")
        print("3. PubMed            (Under Construction)")
        print("4. Exit")
        search_engine = input("Pls type pure number: ")
        if (search_engine == '4'):
            SystemExit()

        elif (search_engine == '1'):
            while(True):
                content = input ("Please type your your search content: ")
                print("You want to search: " + content + ' , Right?')
                ieee_confirm = input('Enter [y] to Confirm or back to Previous Menu: ')
                if (ieee_confirm == "Y" or ieee_confirm == "y"):
                    ieee = ixs.XploreSpider(content)
                    ieee.operate()
                    ieee_loop = input("Do you want to continue searching? Enter [y] to continue or back to Previous Menu: ")
                    if (ieee_loop != 'y') :
                        break
                else:
                    break




        # search_title = r'("online risk*” OR "online abuse" OR "mental health") AND "deep learning"'
        # ieee = ixs.XploreSpider(search_title)
        # ieee.operate()