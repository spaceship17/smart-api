import kaggle

print(kaggle.api.dataset_list_files('yousefsaeedian/financial-q-and-a-10k').files)

kaggle.api.authenticate()

kaggle.api.dataset_download_files('yousefsaeedian/financial-q-and-a-10k', path = '.' , unzip = True  )

kaggle.api.dataset_metadata('yousefsaeedian/financial-q-and-a-10k', path = '.' )


datasets =  kaggle.api.dataset_list(search='flight price')

print(datasets)
