class Chains:
    """
    Markov Chains that will allow for generation of poems.
    """
    def __init__(self, order, filename, length):
        if (order < 2):
            self.order = 2
        elif (order > 6):
            self.order = 6
        else:
            self.order = order
        self.filename = filename
        self.length = length
        self.group_size = self.order + 1
        self.text = None
        self.graph = {}
        self.poem = None
        
        self._train(filename = self.filename)
        self._generate(length = self.length)
        
    def _train(self, filename):
        """
        Prepare the instance of all possible word combinations, depending on the order they are combined in.
        """
        self.text = open(filename, "r", encoding="utf-8").read().split()
        self.text = self.text + self.text[:self.order]
        
        for i in range(0, len(self.text) - self.group_size):
            key = tuple(self.text[i : i + self.order])
            value = self.text[i + self.order]
            
            if key in self.graph:
                self.graph[key].append(value)
            else:
                self.graph[key] = [value]
                
    def _generate(self, length):
        """
        Generate the poems
        """
        # Chose a random place to start
        import random
        index = random.randint(0, len(self.text) - self.order)
        result = self.text[index : index + self.order]
        
        for i in range(length):
            state = tuple(result[len(result) - self.order:])
            next_word = random.choice(self.graph[state])
            result.append(next_word)
            
        self.poem = " ".join(result[self.order:])
        
    def getPoem(self, rest = False):
        """
        Return the poem to the user.
        @rest - should the output be in a REST API form or not.
        """
        if not rest:
            output_message = []
            inner_message = []
            i = 1
            for word in self.poem.split():
                if (i % 50 == 0):
                    temp_line = word + "..."
                    inner_message.append(temp_line)
                    output_message.append("".join(inner_message))
                    continue
                if (i % 5 == 1):
                    temp_line = word[0].upper() + word[1:] + " "
                    inner_message.append(temp_line)
                    i += 1
                    continue
                if (i % 20 == 0):
                    temp_line = word + "."
                    inner_message.append(temp_line)
                    output_message.append("".join(inner_message))
                    inner_message = []
                    i+= 1
                    continue
                if (i % 5 == 0):
                    temp_line = word + ","
                    inner_message.append(temp_line)
                    output_message.append("".join(inner_message))
                    inner_message = []
                    i += 1
                    continue
                else:
                    temp_line = word + " "
                    inner_message.append(temp_line)
                    i += 1
                    continue
            self.poem = output_message
            return self.poem
        else:
            output_message = ""
            i = 1
            for word in self.poem.split():
                if (i % 5 == 1):
                    output_message += word[0].upper() + word[1:] + " "
                    i += 1
                    continue
                if (i % 20 == 0):
                    output_message += word + ". "
                    i+= 1
                    continue
                if (i % 5 == 0):
                    output_message += word + ", "
                    i += 1
                    continue
                else:
                    output_message += word + " "
                    i += 1
                    continue
            output_message = output_message[:-2] + "..."
            self.poem = output_message
            output_information = {"order" : self.order,
                                  "words_quantity" : self.length,
                                  "poem" : self.poem,
                                  "conversion_tool": "https://www.online-toolz.com/tools/text-unicode-entities-convertor.php"}  
            return output_information
        