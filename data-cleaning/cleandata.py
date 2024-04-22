# Mengetahui shape dari dataset
df_bankpromo.shape

# Mengetahui info nama column dan data type di dataset
df_bankpromo.info()

# Mengubah data type Account id
df_bankpromo['ACCOUNT_ID'] = df_bankpromo['ACCOUNT_ID'].astype(str)
