import pandas as pd

from features import FeatureExtraction


def main():
    df = pd.read_csv("data.csv")
    i: int = 0

    datas = []

    for d in df.iterrows():
        print(d[1]["Domain"])

        features = FeatureExtraction(d[1]["Domain"])

        data = features.getFeaturesList()

        data.insert(0, d[1]["Domain"])
        label: int = 1

        if d[1]["Label"] != 1:
            label = 0

        data.insert(32, label)
        print(data)
        datas.append(data)

    newData = pd.DataFrame(
        datas,
        columns=[
            "Domain",
            "UsingIP",
            "LongURL",
            "ShortURL",
            "Symbol@",
            "Redirecting",
            "PrefixSuffix",
            "SubDomains",
            "HTTPS",
            "DomainRegLen",
            "Favicon",
            "NonStdPort",
            "HTTPSDomainURL",
            "RequestURL",
            "AnchorURL",
            "LinksInScriptTags",
            "ServerFormHandler",
            "InfoEmail",
            "AbnormalURL",
            "WebsiteForwarding",
            "StatusBarCust",
            "DisableRightClick",
            "UsingPopupWindow",
            "IframeRedirection",
            "AgeofDomain",
            "DNSRecording",
            "WebsiteTraffic",
            "PageRank",
            "GoogleIndex",
            "LinksPointingToPage",
            "StatsReport",
            "class",
        ],
    )

    newData.to_csv("dataset.csv")


main()
