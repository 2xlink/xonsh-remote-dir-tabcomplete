def remoteDirCompleter(prefix, line, begindx, endidx, ctx):
    import re, subprocess
    result = re.findall("[A-Za-z]+:[^:]*", prefix)

    if result: # is not empty
        hostName, path = result[0].split(":")
        if not path: # is empty
            path = ""

        fileList = re.split("\n", $(ssh @(hostName) ls -d1FL @(path + "*")))

        fileList = filter(lambda x: x != '', fileList)

        fileList = map(lambda x: hostName + ":" + x, fileList)

        return set(fileList)

    return None