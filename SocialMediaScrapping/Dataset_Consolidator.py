import csv

"""
converts .csv files created from RedditScrapper.py into a single dataset csv

@param new_dataset_name: the desired name for the consolidated dataset
@param *old_datasets: any amount of csv files to be consolidated 
"""
def consolidate_dataset(new_dataset_name: str, *old_datasets: csv):
    
    new_dataset = {
        'post': [],
        'subreddit': []
    }

    # keys used to validate data
    key = {
        'buildapc': 0,
        'nutrition': 1
    }

    # iterate through old datasets
    for dataset in old_datasets:

        with open(dataset, 'r', encoding='utf8') as data:
            # skip headerline
            next(csv.reader(data))
            for row in csv.reader(data):
                # strips post of all next lines and commas
                new_dataset['post'].append(str(row[7]).replace("\n", "").replace(",", ""))
                new_dataset['subreddit'].append(str(row[4]))

    # create new dataset csv
    with open(new_dataset_name + '.csv', 'w', encoding='utf8') as f:
        #f.write('post,subreddit\n')
        for i in range(len(new_dataset['post'])):
            if new_dataset['subreddit'][i] in key.keys():
                f.write('"' + (str(new_dataset['post'][i])) + '"' + "\n") #"," + str(key[new_dataset['subreddit'][i]]) + "\n")

def main():


    pc_hot = "How to Build a PC Dataset/Hot_500_Build_A_PC_Posts.csv"
    pc_top = "How to Build a PC Dataset/Top_500_Build_A_PC_Posts.csv"


    nutrition_hot = "Nutrition Dataset/Hot_500_Nutrition_Posts.csv"
    nutrition_top = "Nutrition Dataset/Top_500_Nutrition_Posts.csv"

    consolidate_dataset("PC 1000 Post Training Dataset", pc_hot, pc_top)
    consolidate_dataset("Nutrition 1000 Post Dataset", nutrition_hot, nutrition_top)


if __name__ == "__main__":
    main()