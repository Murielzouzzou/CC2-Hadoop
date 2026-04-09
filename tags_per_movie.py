from mrjob.job import MRJob                                                               
                                                                                          
                                                                                          
                                                                                          
class TagsPerMovie(MRJob):                                                                
                                                                                          
                                                                                          
                                                                                          
    def mapper(self, _, line):                                                            
                                                                                          
        try:                                                                              
                                                                                          
            userId, movieId, tag, timestamp = line.split(',')                             
                                                                                          
            yield movieId, 1                                                              
                                                                                          
        except:                                                                           
                                                                                          
            pass                                                                          
                                                                                          
                                                                                          
                                                                                          
    def reducer(self, key, values):                                                       
                                                                                          
        yield key, sum(values)                                                            
                                                                                          
                                                                                          
                                                                                          
if __name__ == '__main__':                                                                
                                                                                          
    TagsPerMovie.run()    