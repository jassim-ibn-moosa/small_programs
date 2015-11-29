def panagram(sentence):
    for l in 'abcdefghijklmnopqrstuvwxyz':
        if l not in sentence:
            return False
    return True
    

print panagram("the quick brown fox jumps over the lazy dog")
print panagram("toys")
print panagram("a")
print panagram("abcdefghijkl;mnopqrstuvwxy")
