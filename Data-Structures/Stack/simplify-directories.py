# SIMPLIFIED PATH [DIRECTORY] :
def simplifyPath(path: str) -> str:
    splitter = '/'.join(path.split())
    directories = splitter.split('/')
    print(directories)
    stack = []
    for files in directories:
        if files == '' or files == '.' or files == 'cd':
            continue
        elif files == '..':
            if stack:
                stack.pop()
        else:
            stack.append(files)
    return '/'.join(stack)

file_path = input()
print(simplifyPath(file_path))