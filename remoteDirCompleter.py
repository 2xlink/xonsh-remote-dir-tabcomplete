def remoteDirCompleter(prefix, line, begindx, endidx, ctx):
    import re
    result = re.findall("[A-Za-z]+:[A-Za-z0-9/]*", prefix)

    if result: # is not empty
        hostName, path = result[0].split(":")
        if not path: # is empty
            path = "/"

        fileList = re.split("\n", $(ssh @(hostName) find @(path)* -maxdepth 0))

        if fileList == ['']:
            return None

        return set(fileList)
    return None