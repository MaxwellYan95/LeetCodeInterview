def simplifyPath(path: str) -> str:
    lst = path.split("/")
    pathLst = []
    for element in lst:
        if element != '' and element != '.':
            if element == "..":
                pathLst = pathLst[0: len(pathLst)-1]
            else:
                pathLst.append(element)
    return "/" + "/".join(pathLst)
print(simplifyPath("/.../a/../b/c/../d/./"))