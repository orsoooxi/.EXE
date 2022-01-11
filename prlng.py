def prlng(code):
    if "echo" in code:
        print(code[4:len(code)])
    if "=" in code:
        varname = code[0]
        varval = code[2:(len(code))]
        jsonvar = {
            "name": varname,
            "value": varval
        }
        return(jsonvar)
i = prlng("i=hi")
print(i)
