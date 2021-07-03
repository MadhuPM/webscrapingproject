mport requests
from bs4 import BeautifulSoup


products_to_track =[
    {

        "product_url":"https://www.flipkart.com/samsung-galaxy-m42-prism-dot-black-128-gb/p/itmb137b3296810c?pid=MOBG3KGVVVVZ6YHF&lid=LSTMOBG3KGVVVVZ6YHFXR7PJE&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_532df9b7-15bd-49f2-b46b-ff3841de2126_1_1BUWY8OBA8L9_MC.MOBG3KGVVVVZ6YHF&ppt=clp&ppn=mobile-phones-store&ssid=cgd91tah4w0000001625217865787&otracker=clp_pmu_v2_Latest%2BSamsung%2Bmobiles%2B_2_1.productCard.PMU_V2_SAMSUNG%2BGalaxy%2BM42%2B%2528Prism%2BDot%2BBlack%252C%2B128%2BGB%2529_samsung-mobile-store_MOBG3KGVVVVZ6YHF_neo%2Fmerchandising_1&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Latest%2BSamsung%2Bmobiles%2B_LIST_productCard_cc_2_NA_view-all&cid=MOBG3KGVVVVZ6YHF",
        "name": "SAMSUNG Galaxy M42 (Prism Dot Gray, 128 GB)  (8 GB RAM)",
        "target_priice":25000
    },
    {
         "product_url":"https://www.flipkart.com/samsung-galaxy-m42-prism-dot-gray-128-gb/p/itmb137b3296810c?pid=MOBG3KGVPW53GUV4&lid=LSTMOBG3KGVPW53GUV45HDXNX&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_532df9b7-15bd-49f2-b46b-ff3841de2126_1_1BUWY8OBA8L9_MC.MOBG3KGVPW53GUV4&ppt=clp&ppn=mobile-phones-store&ssid=cgd91tah4w0000001625217865787&otracker=clp_pmu_v2_Latest%2BSamsung%2Bmobiles%2B_1_1.productCard.PMU_V2_SAMSUNG%2BGalaxy%2BM42%2B%2528Prism%2BDot%2BGray%252C%2B128%2BGB%2529_samsung-mobile-store_MOBG3KGVPW53GUV4_neo%2Fmerchandising_0&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Latest%2BSamsung%2Bmobiles%2B_LIST_productCard_cc_1_NA_view-all&cid=MOBG3KGVPW53GUV4",
         "name":"SAMSUNG Galaxy M42 (Prism Dot Black, 128 GB)  (8 GB RAM)",
        "target_price":21000

    },
    {
          "product_url":"https://www.flipkart.com/samsung-galaxy-m12-blue-128-gb/p/itme593a120f429d?pid=MOBGFZUHYABADANE&lid=LSTMOBGFZUHYABADANEXXSONA&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_532df9b7-15bd-49f2-b46b-ff3841de2126_1_1BUWY8OBA8L9_MC.MOBGFZUHYABADANE&ppt=clp&ppn=mobile-phones-store&ssid=cgd91tah4w0000001625217865787&otracker=clp_pmu_v2_Latest%2BSamsung%2Bmobiles%2B_4_1.productCard.PMU_V2_SAMSUNG%2BGalaxy%2BM12%2B%2528Blue%252C%2B128%2BGB%2529_samsung-mobile-store_MOBGFZUHYABADANE_neo%2Fmerchandising_3&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Latest%2BSamsung%2Bmobiles%2B_LIST_productCard_cc_4_NA_view-all&cid=MOBGFZUHYABADANE",
           "name":"SAMSUNG Galaxy M12 (Blue, 128 GB)  (6 GB RAM)",
        "target_price":13000
    },
    {
        "product_url":"https://www.flipkart.com/oppo-a54-moonlight-gold-128-gb/p/itm2c71eaacf710e?pid=MOBG23KTD7YWGYMZ&lid=LSTMOBG23KTD7YWGYMZXCBXBG&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=clp_banner_1_15.bannerX3.BANNER_oppo-fantastic-days-lp4rg7uj4-store_GS09TX2Y6BPI&fm=neo%2Fmerchandising&iid=737c0fba-d7f7-4af0-959a-b6debb28017c.MOBG23KTD7YWGYMZ.SEARCH&ppt=clp&ppn=oppo-fantastic-days-lp4rg7uj4-store&ssid=9gufoqqohc0000001625225966734",
        "name":"OPPO A54 (Moonlight Gold, 128 GB)  (6 GB RAM)",
        "target_price":16000
    },
    {
        "product_url":"https://www.flipkart.com/realme-8-5g-supersonic-black-128-gb/p/itm8a548578d136e?pid=MOBG24GTTRD9XB8X&lid=LSTMOBG24GTTRD9XB8XCHSEML&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_13&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_realme_mobile-phones-store_0JN61DYS7W5I_wp3&fm=neo%2Fmerchandising&iid=6a821ee0-f9dc-4726-994e-e5580d89118f.MOBG24GTTRD9XB8X.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=sjrd9rtj680000001625226025925",
        "name":"realme 8 5G (Supersonic Black, 128 GB)  (4 GB RAM)",
        "target_price":15000
    }
]
def give_product_price(url):
    headers = {
        'user_agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    product_price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})

    return product_price.getText()

result_file=open("My_result_file.txt","w")

try:

    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + "-" + every_product.get("name"))
        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))
        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("available at your required price")
            result_file.write(
                every_product.get(
                    "name") + " - \t" + " available at target price " + "current price-"  + str(my_product_price) +'\n')
        else:

            print("still at current price")

finally:
    result_file.close()






