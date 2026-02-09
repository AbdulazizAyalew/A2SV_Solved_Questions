class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Romans_equivalent = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM",2:"II",3:"III",20:"XX",30:"XXX",200:"CC",300:"CCC",2000:"MM",3000:"MMM",6:"VI",7:"VII",8:"VIII",60:"LX",70:"LXX",80:"LXXX",600:"DC",700:"DCC",800:"DCCC"}
        deduct = [500,100,50,10,5,1]
        Roman_num = []
        str_num = str(num)
        pos = len(str_num) - 1
        i = 0
        while pos >= 0:
            num_to_convert = int(str_num[i]) * (10 ** pos)
            if str_num[i] == "4" or str_num[i] == "9":
                Roman_num.append(Romans_equivalent[num_to_convert])
            else:
                if num_to_convert in Romans_equivalent:
                    Roman_num.append(Romans_equivalent[num_to_convert])
            
            pos -= 1
            i += 1
        
        return "".join(Roman_num)


                        

