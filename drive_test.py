import win32api

drives = win32api.GetLogicalDriveStrings()
h = [x.rstrip("\\") for x in drives.split('\000') if x]
print(h)