import dropbox
import os

class TransferData:
    def __init__(self, token):
        self.token = token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.token)
        for root, dirs, files in os.walk(file_from):
            for file in files:
                print(root, file)
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    token = "sl.BLWINjUa5Zu5VG7AdS2DiRCqM8Q4svWXls_1OUu_rufln2Lvb9odFUkESzGQlelwXhRe9ym1MgQJCzPnbD6Gr52YYfEjml3ATg2txbH1dm4G1ozruIHuXiOgZrGXgpiIKQN5VW4"
    transferData = TransferData(token)
    file_from = input("Enter path to transer from: ")
    file_to = input("Enter path to transfer to")
    transferData.uploadFile(file_from, file_to)
    print("data transfered")
main()