def remoteDirCompleter(prefix, line, begindx, endidx, ctx):
    import re
    result = re.findall("[A-Za-z]+:[^:]*", prefix)

    if result: # is not empty
        hostName, path = result[0].split(":")

        # Get matching files
        fileList = re.split("\n", $(ssh @(hostName) ls -d1FL @(path + "*")))

        # Remove empty entries
        fileList = filter(lambda x: x != '', fileList)

        # Escape spaces
        fileList = map(lambda x: x.replace(" ", "\\ "), fileList)

        # Prefixes the suggestions with the host name
        fileList = map(lambda x: hostName + ":" + x, fileList)

        return set(fileList)

    return None