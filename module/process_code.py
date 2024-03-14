''' 아무 내용이 없는 줄은 제거합니다. '''
def get_rid_of_empty(c):
    clean = []
    splitted = c.split('\n')
    for s in splitted:
        if len(s.strip()) > 0:
            clean.append(s)
    return '\n'.join(clean)

def remove_semicolon(s):
    """
    Replace all semicolon to \n
    """
    s = s.replace(';','\n')
    return s

def remove_type(s):
    s = s.replace('void', '')
    s = s.replace('const', '')
    return s

def clean_comments(s):
    """
    Remove sharp-leading comments from the beginning and any other place
    """
    lines = s.split('\n')
    flag = False
    clean = []
    for line in lines:

        # /* is procceeding
        if flag:
            if '*/' not in line:
                continue
            line = line[line.index('*/')+2:].rstrip()
            flag = False

        if line.lstrip().startswith('//'):
            continue

        if line.lstrip().startswith('/*'):
            if '*/' not in line:
                flag = True
            continue

        if '//' in line:
            line = line[:line.index('//')].rstrip()

        clean.append(line)
    return '\n'.join(clean)

def clean_lex(s):
    """Remove `using namespace`"""
    lines = s.split('\n')
    clean = []
    for line in lines:
        if 'using namespace' in line:
            continue
        clean.append(line)    
    return '\n'.join(clean)

def clean_indents(s):
    """
    Replace all types of spaces
    """
    return ' '.join(s.split())

def preproc(s):
    """Apply all cleaning functions"""
    s = remove_semicolon(s)
    s = remove_type(s)
    s = clean_comments(s)
    s = clean_lex(s)
    s = get_rid_of_empty(s)
    s = clean_indents(s)
    return s