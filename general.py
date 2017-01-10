import os


# Each website crawled has a different folder
def createProjectDir(directory):
    if not os.path.exists(directory):
        print('Creating project '+ directory)
        os.makedirs(directory)

# Create queue and crawled files
def createDataFiles(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        writeFile(queue, base_url)
    if not os.path.isfile(crawled):
        writeFile(crawled, '')

# Create a new file
def writeFile(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
# Add data onto an existing file
def appendToFilePath(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')

# Delete the contents of a file
def deleteFileContents(path):
    with open(path, 'w'):
        pass

# Read a file and convert each line to set items
def fileToSet(path):
    results = set()
    with open(path,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

# Iterate through a set, each item in the set will be a new line in the file
def setToFile(links, f):
    deleteFileContents(f)
    for link in sorted(links):
        appendToFilePath(f, link) 


