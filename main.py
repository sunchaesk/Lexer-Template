### pdb
# import pdb; pdb.set_trace()

# symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ','] # single-char keywords
symbols_map = {'{':'tk_OpenBrace',
               '}':'tk_CloseBrace',
               '(':'tk_OpenBracket',
               ')':'tk_CloseBracket',
               '[':'tk_OpenSquareBracket',
               ']':'tk_CloseSquareBracket',
               '.':'tk_Dot',
               '"':'tk_DoubleQuote',
               '\'':'tk_SingleQuote',
               '*':'tk_Mult',
               '\n':'tk_Newline',
               '/':'tk_Div',
               '%':'tk_Modulo',
               ':':'tk_Colon',
               ',':'tk_Comma'}
#other_symbols = ['\\', '/*', '*/'] # multi-char keywords
other_symbols_map = {'\\':'tk_SingleLineComment',
                     '/*':'tk_OpenMultiComment',
                     '*/':'tk_CloseMultiComment'}
#keywords = ['for', 'if', 'elif', 'else']
word_map = {'for':'tk_For',
            'if':'tk_If',
            'elif':'tk_Elif',
            'else':'tk_Else'}
#KEYWORDS_DICT = dict(symbols_map.items() + other_symbols_map.items() + keywords_map.items())
KEYWORDS_MAP = {
    'for':'tk_For',
    'if':'tk_If',
    'elif':'tk_Elif',
    'else':'tk_Else',
    '\\':'tk_SingleLineComment',
    '/*':'tk_OpenMultiComment',
    '*/':'tk_CloseMultiComment',
    '{':'tk_OpenBrace',
    '}':'tk_CloseBrace',
    '(':'tk_OpenBracket',
    ')':'tk_CloseBracket',
    '[':'tk_OpenSquareBracket',
    ']':'tk_CloseSquareBracket',
    '.':'tk_Dot',
    '"':'tk_DoubleQuote',
    '\'':'tk_SingleQuote',
    '*':'tk_Mult',
    '\n':'tk_Newline',
    '/':'tk_Div',
    '%':'tk_Modulo',
    ':':'tk_Colon',
    ',':'tk_Comma',
}
KEYWORDS = list(symbols_map.keys()) + list(other_symbols_map.keys()) + list(word_map.keys())

def scan(string: str):
    """
    - read input string
    - output list of tokens
    """
    white_space = ' '
    lexeme = ''
    scanned_list= []
    for i,char in enumerate(string):
        if char != white_space:
            lexeme += char # adding a char each time
            if (i+1 < len(string)): # prevents error
                if string[i+1] == white_space or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
                    if lexeme != '':
                        print(lexeme.replace('\n', '<newline>'))
                        scanned_list.append(lexeme.replace('\n', '<newline>'))
                        lexeme = ''
    if lexeme:
        print(lexeme)
        scanned_list.append(lexeme.replace('\n', '<newline>'))
        print(scanned_list)
    return scanned_list

class Token:
    iden = '' #id of token eg: tk_brace
    iden_literal = '' #literal id eg '{'
    keyword = False
    def __init__(self, iden, literal, keyword):
        self.iden = iden
        self.iden_literal = literal
        self.keyword = keyword


def to_token_list(scanned_list: list):
    """
    input: a list of scanned strings
    output: a list of tokens
    """
    tok_list = []
    for s in scanned_list:
        if s in KEYWORDS_MAP:
            temp_class = Token(s, KEYWORDS_MAP[s], True)
            tok_list.append(temp_class)
        else:
            temp_class = Token(s, s, False)
            tok_list.append(temp_class)
    return tok_list


if __name__ == "__main__":
    ll = to_token_list(scan("for (int i = 0)"))
    print(ll)
