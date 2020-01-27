def spam():
    eggs = 'spam local'
    print(eggs) #prints the above

def bacon():
    eggs = 'bacon local'
    print(eggs)#prints the bacon local
    spam()
    print(eggs) # also prints bacon local

eggs = 'global'
bacon()
print(eggs) # prints global
