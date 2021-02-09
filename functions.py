def complexFunction(s,*mult,**amt):
    sum = 0
    for x in mult:
       sum = sum +x 
    print("the legends name is: ",s,"\n %s, the total sum we have gathered is %d"%(s,sum),"and list is as follows")
    for i,j in amt.items():
        print("Person",i,"Amount",j)
print(complexFunction("sairam",550,650,750,850,peter = 550, john = 650, mark = 750, chris = 850)
)

''' keyword def introduces function definition. followed by function name
    first statement in function body is optional statement called documentation strings
    function execution introduces a nre symbol table used for the local variables of the function
    all local variables in the function are stored in this table whereas variable references first 
    look in the local symbol table then in the local symbol table of enclosing function, then in the
    global symbol table and finally in the table of buitl-in names.
    '''
    