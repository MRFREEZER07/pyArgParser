

class Argparser:
     
    def __init__(self,args):
        """  
        args:
            self.args from exc file
        """
       
        self.commands =[]
        self.options =[]
        self.optionValues ={} #(userOPtions)dict or set has unique index/no repeat value
        self.args=args
        #print(self.args)

        for arg in self.args:
            if "-" in arg:
                """
                seperating argument or option with value
                arg -> -h or --help
                optionwithvalue -> -format=json
                """
                if "=" in arg:
                    #option with value
                    pair =arg.split('=')
                    self.optionValues[pair[0]]=pair[1]
                    self.options.append(pair[0])

                else:
                   
                    #option
                    self.options.append(arg)
            else:
                self.commands.append(arg)



    #arg.hasOptions("-p","-l")
    def hasOptions(self,options: list):
        userOptions =set(self.options)
        reqiredOptions=set(options) #programmerOptions
        return list(reqiredOptions & userOptions)

    def hasOption(self,option):
        return option in self.hasOptions([option])

    def hasOptionValue(self,option):
        return option in self.optionValues



    def hasCommands(self,command):
        userCommands =set(self.commands)
        requiredCommands=set(command)
        return list(userCommands & requiredCommands)

    def hasCommand(self,command):
        return command in self.hasCommands([command])



    def getOptionValue(self,option ,default=None):
        if option in self.optionValues:
            return self.optionValues[option] #return key
        else:                                                                                                           
            return default


    def printHelp(self,file):
        """this function print help from the assets folder

        Args:
            file (txt): call printHelp(filename)
            example :printHelp("help") 
        """

        with open("assets/"+file+'.txt') as f:
            lines =f.read()
            print("\n"+lines)
            exit(-1)

    def printBanner(self):
        """print Banner.txt file from the assets folder
        """
        try:
            with open("assets/banner.txt") as f:
                lines= f.read()
                print('\n '+lines)
                exit(-1)
        except FileNotFoundError as e:
            print(e)
            