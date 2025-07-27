a = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

print("단어 목록:", a)

long_word= max(a, key=len)
print(f"가장 긴 단어: {long_word} ({len(long_word)}글자)")

short_word = min(a, key=len)
print(f"가장 짧은 단어: {short_word} ({len(short_word)}글자)")