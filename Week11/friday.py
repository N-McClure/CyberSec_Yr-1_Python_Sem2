# Talking about Regular Expressions today:
# NOTE: There is a built in module for regular expressions, called "re" which must be imported.

# Symbol Meanings:
    # ^: Start of line
    # $: End of line
    # \w: Matches any word character (equal to [a-zA-Z0-9_])
    # \d: Matches any digit (equal to [0-9])
    # \b: Boundary character (equal to [a-zA-Z0-9 _])
    # \s: Matches any whitespace character (equal to [ \t\n\r\f\v])
    # \.: Matches any character except a newline
    # | : OR operator
    # (): Grouping parentheses
    # []: Character set
    # [^]: Negation character set
    # *: Matches zero or more of the preceding element
    # +: Matches one or more of the preceding element
    # ?: Matches zero or one of the preceding element
    # {n}: Matches exactly n occurrences of the preceding element
    # {n,m}: Matches at least n but not more than m occurrences of the preceding element
    # {n,}: Matches at least n occurrences of the preceding element

# Imported Libraries:
import re

if __name__ == '__main__':
    print("running...")
    
    # Regular Expression Examples:
    
    # NOTE: findall(pattern, string, flag = 0) -> finds all occurances of a pattern in a string.
    string = "I love BACON!, BACON IS THE BEST!!!, THERE IS NOTHING BETTER THAN BACON.bacon baCon BaCON "
    bacon = re.findall('BACON', string)
    print("Occurrences of 'BACON' in the string:", bacon)
    
    bacon = re.findall('BACON',string, flags=re.IGNORECASE)
    print("Occurrences of 'BACON' in the string:", bacon)
    
    print(re.findall(r'.A.', string))
    
    # NOTE: search(pattern, string, flag = 0) -> finds the first occurance of a pattern in a string.
    s = re.search('\s',string)
    print(s)
    print("First space in the string:", s.start())
    
    # NOTE: split(pattern, string, maxsplit=0, flags=0) -> splits the string by the occurance of a pattern.
    words = re.split('\s', string)
    print("Words in the string:", words)
    
    words = re.split('\s', string, maxsplit=2)
    print("Words in the string (limited to 2):", words)
    
    # NOTE: sub(pattern, repl, string, count=0, flags=0) -> replaces all occurrences of a pattern in a string with a replacement.
    new_string = re.sub('BACON', 'Bacon', string)
    print("New string with 'BACON' replaced with 'Bacon':", new_string)
    
    new_string = re.sub('BACON', 'Protein', string, flags=re.IGNORECASE)
    print("New string with 'BACON' replaced with 'Protein' (ignoring case):", new_string)
    
    # NOTE: match(pattern, string, flags=0) -> finds the pattern at the beginning of the string.
    m = re.match('BACON', string, flags=re.IGNORECASE)
    print(m)
    if m:
        print("Match found at start of the string")
    else:
        print("No match found at start of the string.")
    
    # NOTE: fullmatch(pattern, string, flags=0) -> finds the pattern at the beginning of the entire string.
    m = re.fullmatch('^BACON$', string, flags=re.IGNORECASE)
    print(m)
    if m:
        print("Full match found at start of the string")
    else:
        print("No full match found at start of the string.")