import requests

postcode_string = 'class="postal-code">'

def get_centers(postcode):
    try:
        page_text = requests.post("https://www.gov.uk/find-mot-course", data={"postcode": postcode}).text
        print(1)
        return ",".join([f"{x.split('<')[0]}:{x.split(postcode_string)[1].split('<')[0]}" for x in page_text.split("govuk-heading-s govuk-!-display-inline\">")[1:]])
    except:
        print(2)
        return "Unable to find centers"

with open("postcodes.txt", "r") as r:
    postcodes = r.read().splitlines()

with open("centers.txt", "w") as w:
    w.write("\n".join([get_centers(x) for x in postcodes]))
