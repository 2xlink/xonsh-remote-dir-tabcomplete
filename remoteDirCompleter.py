def remoteDirCompleter(prefix, line, begindx, endidx, ctx):
    import re
    result = re.findall("[A-Za-z]+:[^:]*", prefix)

    if result: # is not empty
        hostName, path = result[0].split(":")
        if not path: # is empty
            path = "/"

        fileList = re.split("\n", $(ssh @(hostName) find @(path)* -maxdepth 0 ))

        fileList = filter(lambda x: x != '', fileList)

        fileList = map(lambda x: hostName + ":" + x, fileList)

        return set(fileList)
    return None