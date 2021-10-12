import dropbox

import os
for root, dirs, files in os.walk(".", topdown=True):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

class TransferData:
    def __init__(self, access_token):
        self.access_token= access_token

    def uploadFile(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)

        file_handler= open(file_from, 'rb')
        dbx.files_upload(file_handler.read(), file_to)

def main():
    access_token='sl.A3rNwYNvzfkHICIf-8_8APXf66torvvf3ODxEHMSwCPvB_0ucFjLAfcJo0zWH9oSwl68l8cjNSxRUW6V0OaOMuuwtAaGorlVL8KFJK2O5GoHHFm2v7A68bWjpnQrJT0I0qTNB0k4c-w'
    transferData= TransferData(access_token)

    file_from= input('write down your file path ....: ')
    file_to= input('enter the name of the file : ')
    file_to='/testFolder/'+ file_to
    

    transferData.uploadFile(file_from, file_to)
    print('file transfered succesfully!')

main()


#'sl.A3rNwYNvzfkHICIf-8_8APXf66torvvf3ODxEHMSwCPvB_0ucFjLAfcJo0zWH9oSwl68l8cjNSxRUW6V0OaOMuuwtAaGorlVL8KFJK2O5GoHHFm2v7A68bWjpnQrJT0I0qTNB0k4c-w'




     
    