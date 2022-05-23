PROTOCOL = "Protocol"
ASTROMECH = "Astromech"

PROTOCOL_PARTS = ["p_head", "p_chassis", "p_left_arm", "p_right_arm", "p_left_leg", "p_right_leg"]
ASTROMECH_PARTS = ["a_dome", "a_body", "a_left_leg", "a_center_leg", "a_right_leg"]

#DEFINE A CLASS for a droid that has a serial num, type, and a collection of psrts
#define slots and write a constructor
#what dats struct can we use to wuickly determine whether or not a specific part is needed
#and whether or not it has already been installed
class Droids:
    __slots__ = ["__serial_num", "__type", "__parts", "__installed"]
    def __init__(self, serial_num, type):
        self.__parts = dict()
        self.__serial_num = serial_num
        self.__type = type
        self.__installed = 0
        if type == PROTOCOL:
            for part in PROTOCOL_PARTS:
                self.__parts[part] = False
        elif type == ASTROMECH:
            for part in ASTROMECH_PARTS:
                self.__parts[part] = False
        else:
            raise ValueError("Not a valid droid type: " + type)
    #a method that returns True if a specific part is needed by the droid 
    def needs_part(self, a_part):
        if a_part in self.__parts:
            return not self.__parts[a_part]
        else:
            return False


    #function that installs a part; raise a value error if the part is not needed, install otherwise
    def install(self, a_part):
        if self.needs_part(a_part):
            self.__parts[a_part] = True
            self.__installed +=1
        else:
            raise ValueError("part is not needed in this droid: " + a_part)
    
    #a function that returns True if the droid is finished, and False is not
    def is_complete(self):
        return self.__installed == len(self.__parts)

        # for part in self.__parts:
        #     if not self.__parts[part]:
        #         return False
        # return True
    def __repr__(self):
        string = "Droid:" \
            + "\n serial number: " + self.__serial_num
        for part in self.__parts[part]:
            string += "installed"
        else:
            string += "missing"
        return string
    def __str__(self):
        return "Droid Serial Num:", self.__serial_num, "is complete: ", self.is_complete

def main():
    proto = Droids("C3P0", PROTOCOL)
    print(proto)
    print(repr(proto))
if __name__ == "__main__":
    main()