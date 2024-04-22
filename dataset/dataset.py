# Import dataset transaction behaviour (csv format) from google drive

sheet_url = 'https://drive.google.com/file/d/1l-sg91hd2ZLiFzGV2yZY8jJ3v-ksGPJe/view'    #assign link to a variable
sheet_url_replace = 'https://drive.google.com/uc?id=' + sheet_url.split('/')[-2]        #replace the link

print (sheet_url_replace)

df_bankpromo = pd.read_csv(sheet_url_replace)     # Import/read the csv file into pandas dataframe. We name the df = bankpromo
df_bankpromo.head()
