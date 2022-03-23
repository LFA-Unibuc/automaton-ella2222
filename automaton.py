class rejectionException(Exception):
    pass

class Automaton():

    def __init__(self, config_file):
        self.config_file = config_file
        self.sigma = []
        self.states = []
        self.transitions = []
        print("Hi, I'm an automaton!")

    def alfabet(linie, sus, jos):
        l = []
        for i in range(sus, jos):
            cuv = linie[i].split()
            if len(cuv) != 1:
                return False
            l.append(cuv[0])
        return l

    def stari(linie, sus, jos):
        l = []
        nrs = 0
        for i in range(sus, jos):
            cuv = [x.strip() for x in linie[i].split(',')]
            l.append(cuv[0])
            if 'S' in cuv:
                nrs += 1
            if nrs != 1:
                return False
        return l

    def tranzitii(linie, sus, jos):
        l = []
        for i in range(sus, jos):
            cuv = [x.strip() for x in linie[i].split(',')]
            if len(cuv) != 3:
                return False
            l.append((cuv[0], cuv[1], cuv[2]))
        return l

    def validate(self):
        """Return a Boolean

        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """
        with open(self.config_file, "r") as fisier:
            input_str = fisier.read()
            if self.accepts_input(input_str) == False:
                return False
            else:
                for tranzitie in self.transitions:
                    if tranzitie[0] not in self.states or tranzitie[1] not in self.sigma or tranzitie[2] not in self.states:
                        return False
            return True

    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        try:
            self.read_input(input_str)
            return True
        except:
            return False

    def read_input(self, input_str):
        """Return the automaton's final configuration
        
        If the input is rejected, the method raises a
        RejectionException.
        """
        linii = [linie for linie in input_str.split('\n')]
        i = 0
        while i < len(linii):
            if linii[i].startswith('#') or linii[i].startswith('\n'):
                continue
            else:
                sectiune = linii[i].split()[0]
                j = i + 1
                while j < len(linii) and linii[j] != 'End':
                    j += 1
                if sectiune == 'Sigma':
                    self.sigma = Automaton.alfabet(linii, i + 1, j)
                    if self.sigma == False:
                        raise rejectionException()
                else:
                    if sectiune == 'States':
                        self.states = Automaton.stari(linii, i + 1, j)
                        if self.states == False:
                            raise rejectionException()
                    else:
                        if sectiune == 'Transitions':
                            self.transitions = Automaton.tranzitii(linii, i + 1, j)
                            if self.transitions == False:
                                raise rejectionException()
                        else:
                            raise rejectionException()
                i = j
            i += 1


if __name__ == "__main__":
    a = Automaton('date.txt')
    print(a.validate())
