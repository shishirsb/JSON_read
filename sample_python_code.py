import json
import ijson
import csv
techcorp = []
healthcare = []

def process_file():
    with open('sample_json_data', 'rb') as f:
        for item in ijson.items(f, 'contacts.item'):
            if item["digital_footprint"]["emails"][0]["domain"] == "techcorp.ai":
                techcorp.append(
                    [
                        item["contact_id"], item["identity"]["name"]["first"], item["identity"]["name"]["last"],
                        item["digital_footprint"]["emails"][0]["address"], item["professional"]["current"]["position"]["title"],
                        item["professional"]["current"]["company"]["name"]
                    ])
            elif item["digital_footprint"]["emails"][0]["domain"] == 'healthtech.org':
                healthcare.append(
                    [
                        item["contact_id"], item["identity"]["name"]["first"], item["identity"]["name"]["last"],
                        item["digital_footprint"]["emails"][0]["address"],
                        item["professional"]["current"]["position"]["title"],
                        item["professional"]["current"]["company"]["name"]
                    ])

process_file()
print(techcorp)
print(healthcare)

with open('csv_file_Techcorp', 'w', newline ='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for item in techcorp:
        writer.writerow(item)

with open('csv_file_Healthcare', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for item in healthcare:
        writer.writerow(item)


