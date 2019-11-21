class WordDensity:

    def read_file_contents(self, filename):
        with open(filename, "r") as file:
            content = file.read()
        return content

    def total_word_count(self, filename):
        words = self.read_file_contents(filename)
        word_count = len(words.split()) 
        return word_count

    def individual_word_count(self, training_data_file, excluded_words_file):
        word_count = {}
        file_content = self.read_file_contents(training_data_file)
        total_words = file_content.split()
        stopwords_file_content = self.read_file_contents(excluded_words_file)
        stopwords = stopwords_file_content.split()
        for stopword in stopwords: 
            while stopword in total_words:
                total_words.remove(stopword)
        unique_words = list(set(total_words))
        for word in unique_words:
            individual_word_count = total_words.count(word)
            word_count[word] = individual_word_count

        return word_count 

    def word_density(self, training_data_file, excluded_words_file):
        word_density = {}
        total_words= self.total_word_count(training_data_file)
        words = self.individual_word_count(training_data_file, excluded_words_file)
        for word in words:
            density = words[word]/total_words*100
            word_density[word] = density
        return word_density

    def list_top_words(self, training_data_file, excluded_words_file, top_words_count):
        density_list = self.word_density(training_data_file, excluded_words_file)
        top_words = sorted(density_list.items(), key=lambda x: x[1], reverse=True)
        top_words = top_words[: top_words_count]
        return top_words    
