class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        # ex. if val = 1990 then num_parts = [1000, 900, 90, 0] 
        str_val = str(val)
        num_parts = [int(x) * 10**(len(str_val) - i - 1) for i, x in enumerate(str_val)]
        rome = ""

        for x in num_parts:
            match x:
                case 3000:
                    rome += "MMM"
                case 2000:
                    rome += "MM"
                case 1000:
                    rome += "M"
                case 900:
                    rome += "CM"
                case 800:
                    rome += "DCCC"
                case 700:
                    rome += "DCC"
                case 600:
                    rome += "DC"
                case 500:
                    rome += "D"
                case 400:
                    rome += "CD"
                case 300:
                    rome += "CCC"
                case 200:
                    rome += "CC"
                case 100:
                    rome += "C"
                case 90:
                    rome += "XC"
                case 80:
                    rome += "LXXX"
                case 70:
                    rome += "LXX"
                case 60:
                    rome += "LX"
                case 50:
                    rome += "L"
                case 40:
                    rome += "XL"
                case 30:
                    rome += "XXX"
                case 20:
                    rome += "XX"
                case 10:
                    rome += "X"
                case 9:
                    rome += "IX"
                case 8:
                    rome += "VIII"
                case 7:
                    rome += "VII"
                case 6:
                    rome += "VI"
                case 5:
                    rome += "V"
                case 4:
                    rome += "IV"
                case 3:
                    rome += "III"
                case 2:
                    rome += "II"
                case 1:
                    rome += "I"
        return rome

    @staticmethod
    def from_roman(roman_num : str) -> int:
        arab = []
        for x in roman_num:
            match x:
                case "I":
                    arab.append(1)
                case "V":
                    arab.append(5)
                case "X":
                    arab.append(10)
                case "L":
                    arab.append(50)
                case "C":
                    arab.append(100)
                case "D":
                    arab.append(500)
                case "M":
                    arab.append(1000)
                    
        arab_processed = 0
        prev_value = 0
        # we can iterate by reversed list for the sake of avoiding enumerate and try/except
        # it's also faster!
        for x in reversed(arab):
            if x < prev_value:
                arab_processed -= x
            else:
                arab_processed += x
            prev_value = x

        return arab_processed
