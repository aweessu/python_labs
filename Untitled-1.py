data = """Bekzat:google:seo:25,50
Ayan:yandex:sem:12,00
Dias:instagram:social:35,00
Bekzat:google:brand:18,50
Ayan:google:seo:40,00
Dias:yandex:seo:7,50
Bekzat:telegram:social:22,00
Ayan:yandex:brand:30,00
Dias:google:sem:15,00"""

data = data.strip().split("\n")

def parse_order(lines):
    data1 = []
    for i in lines:
        data1.append(i.split(":"))
        data1[-1][3] = float(data1[-1][3].replace(",", "."))
    return data1


def classify_order(source="other", medium="other", amount=0):
    if source == "google" or source == "yandex":
        if medium == "seo" or medium == "sem":
            source_type = "search engines seo"
        elif medium == "brand":
            source_type = "search engines brand"
        else:
            source_type = "other"
    else:
        source_type = "other"
    
    if amount >= 20:
        order_type = "expensive"
    elif amount < 20:
            order_type = "cheap"

    return source_type, order_type


def analyze_orders(data):
    res = dict()
    source_stats = {
            "search engines seo": {
                "orders": ...,
                "total": ...
            },
            "search engines brand": {
                "orders": ...,
                "total": ...
            },
            "other": {
                "orders": ...,
                "total": ...
            }
        }
    for i in parse_order(data):
        name = i[0]
        source = i[1]
        medium = i[2]
        amount = i[3]
        if name not in res:
            res[name] = {"total":0, "orders":0,
                     "expensive":0, "cheap":0}
        res[name]["total"] += amount
        res[name]["orders"] += 1

        source_type, order_type = classify_order(source, medium, amount)
        if order_type == "expensive":
            res[name]["expensive"] += 1
        else:
            res[name]["cheap"] += 1

        
        

    return source_stats

print(analyze_orders(data))
