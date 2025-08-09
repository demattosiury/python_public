# Automation GUI module
import pyautogui as auto
import pyperclip
import time
from items.meele import allmeele

# Set here your browser name and credentials
browserName = 'brave'
email = ''
pwd = ''

# Component position
dialogLoginButton = {'x': 1114, 'y': 144}
dialogEmailLabel = {'x': 598, 'y': 346}
dialogAuthButton = {'x': 793, 'y': 431}

menuItemMarketLabel = {'x': 288, 'y': 629}
itemMarketSearchInput = {'x': 1140, 'y': 270}
itemMarketFirstItem = {'x': 465, 'y': 441}
itemMarketFirstItemPrice = {'x': 789, 'y': 536}

bigAlGunShopLoadMoreItemsStart = {'x': 380, 'y': 577}
bigAlGunShopLoadMoreItemsEnd = {'x': 485, 'y': 577}
bigAlGunShopSelectAll = {'x': 1074, 'y': 623}
bigAlGunShopSellButton = {'x': 425, 'y': 628}

# Other 
gameLink = 'https://www.torn.com'
bigalgunshopLink = 'https://www.torn.com/bigalgunshop.php'
loggedin = False



def isLoggedin():
    auto.hotkey('ctrl','l')
    auto.hotkey('ctrl','c')
    return len(gameLink) == len(pyperclip.paste())

def login():
    # button to open dialog login
    auto.click(dialogLoginButton['x'],dialogLoginButton['y'])
    # email credential
    auto.click(dialogEmailLabel['x'],dialogEmailLabel['y'])
    auto.write(email)
    # password credential
    auto.press('tab')
    auto.write(pwd)
    # auth button
    auto.click(dialogAuthButton['x'],dialogAuthButton['y'])

def buyItemsProcess():
    # go to Item Market
    auto.click(menuItemMarketLabel['x'],menuItemMarketLabel['y'])

    time.sleep(3)

    for meele in allmeele:
        # Item Market search label
        auto.doubleClick(itemMarketSearchInput['x'],itemMarketSearchInput['y'])
        time.sleep(0.5)
        # search the item
        auto.write(meele['name'])
        time.sleep(0.5)
        # select it
        auto.press("tab")
        auto.press("enter")
        time.sleep(1.5)
        
        # start buying items
        while True:
            time.sleep(0.5)
            # first item on market listings
            auto.click(itemMarketFirstItem['x'],itemMarketFirstItem['y'])
            time.sleep(0.5)
            # price of first item
            auto.doubleClick(itemMarketFirstItemPrice['x'],itemMarketFirstItemPrice['y'])
            auto.hotkey('ctrl','c')
            # price data cleaning
            price = pyperclip.paste().replace(',','').replace('$','')
            # if price is lower then item market price
            if float(price) < meele['sell']:
                # buy
                auto.press("tab")
                auto.press("enter")
                auto.press("tab")
                auto.press("enter")
                time.sleep(1.25)
                auto.press("tab")
                auto.press("enter")
            else:
                # go to next item
                break

def sellItemsProcess():
    # go to Big Al Gun Shop
    auto.hotkey('ctrl','l')
    auto.write(bigalgunshopLink)
    auto.press('enter')
    time.sleep(2)
    # go to the end of the page
    auto.press('end')
    time.sleep(1)
    # while exists more items to load
    while True:
        auto.moveTo(bigAlGunShopLoadMoreItemsStart['x'], bigAlGunShopLoadMoreItemsStart['y'])
        auto.mouseDown()
        auto.moveTo(bigAlGunShopLoadMoreItemsEnd['x'], bigAlGunShopLoadMoreItemsEnd['y'], duration=0.5)
        auto.mouseUp()
        auto.hotkey('ctrl','c')
        if len('Load more items') == len(pyperclip.paste()):
            # load more items
            auto.click((bigAlGunShopLoadMoreItemsStart['x']+bigAlGunShopLoadMoreItemsEnd['x'])/2, bigAlGunShopLoadMoreItemsStart['y'])
            time.sleep(2)
            auto.press('end')
            pyperclip.copy('')
        else:
            # sell items
            break
    # sell process
    auto.click(bigAlGunShopSelectAll['x'],bigAlGunShopSelectAll['y'])
    auto.click(bigAlGunShopSellButton['x'],bigAlGunShopSellButton['y'])
    auto.press('tab')
    auto.press('enter')
    time.sleep(2)
    auto.press('home')

# wait x sec before the next pyautogui command
auto.PAUSE = .5

auto.press('win')
auto.write(browserName)
auto.press('enter')
auto.write(gameLink)
auto.press('enter')

# computer sleeps x sec when load game page
time.sleep(5)

# checks if you are logged 
if isLoggedin():
    # if not logged in
    # login process
    login()
    time.sleep(2)

while True:
    time.sleep(2)
    buyItemsProcess()
    time.sleep(2)
    sellItemsProcess()
